"""
Module: recognizer.py
Handles speech capture and transcription using OpenAI Whisper and a microphone.
"""

import os
import os
os.environ["PATH"] = r"C:\ffmpeg\bin;" + os.environ["PATH"]
import tempfile
import time
import whisper
import sounddevice as sd
import soundfile as sf


from exceptions import (
    WhisperModelLoadError,
    AudioCaptureError,
    TranscriptionError,
)
from logger_config import configure_logger

logger = configure_logger()


class SpeechRecognizer:
    """Handles audio capture and transcription using Whisper without PyAudio."""

    def __init__(self, model_size: str = "base", language: str | None = None) -> None:
        """
        Initializes the SpeechRecognizer with a specific Whisper model.

        Args:
            model_size (str): Whisper model size ('tiny', 'base', 'small', 'medium', 'large').
            language (str | None): Language code (e.g., 'en') or None for auto-detection.

        Raises:
            WhisperModelLoadError: If the model fails to load.
        """
        self.model_size = model_size
        self.language = language

        try:
            print(f"Loading Whisper model '{model_size}'...")
            self.model = whisper.load_model(model_size)
            print(f"Model '{model_size}' loaded successfully.")
        except Exception as exc:
            raise WhisperModelLoadError(model_size) from exc

    def capture_audio(self, duration: int = 5, samplerate: int = 16000) -> str:
        print(f"Recording audio for {duration} seconds... Speak now!")

        try:
            recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
            sd.wait()
            if recording.ndim == 1:
                recording = recording.reshape(-1, 1)
        except Exception as exc:
            raise AudioCaptureError("Failed to capture audio from microphone.") from exc

        temp_file_path = None
        try:
            # Use mkstemp to avoid file locking issues on Windows
            fd, temp_file_path = tempfile.mkstemp(suffix=".wav")
            os.close(fd)  # Close the file descriptor immediately

            # Now write to the file by name
            sf.write(temp_file_path, recording, samplerate, subtype='PCM_16')

            print(f"Temporary audio file saved: {temp_file_path}")

            # Now Whisper can open the file
            result = self.model.transcribe(
                audio=temp_file_path,
                fp16=False,
                language=self.language,
                verbose=False,
            )

            return result["text"].strip()

        except Exception as exc:
            raise TranscriptionError(f"Transcription failed. {exc}") from exc

        finally:
            if temp_file_path and os.path.exists(temp_file_path):
                print(f"Temporary file kept at: {temp_file_path}")