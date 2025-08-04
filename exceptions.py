"""
Custom exception classes for the Whisper transcription system.
"""

class WhisperModelLoadError(Exception):
    """Raised when Whisper model fails to load."""
    def __init__(self, model: str):
        super().__init__(f"Failed to load Whisper model '{model}'.")


class AudioCaptureError(Exception):
    """Raised when audio recording fails."""


class TranscriptionError(Exception):
    """Raised when transcription of audio fails."""
