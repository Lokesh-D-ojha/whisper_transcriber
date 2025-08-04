"""
CLI entry point for the Whisper speech recognition system.
"""

from recognizer import SpeechRecognizer
from exceptions import WhisperModelLoadError, AudioCaptureError, TranscriptionError

def main() -> None:
    """
    Main function to execute the Whisper transcription loop.
    """
    print("🎤 Whisper Transcriber CLI")
    print("=" * 40)

    model_size = input("Enter model size (tiny/base/small/medium/large): ").strip().lower()
    if model_size not in ["tiny", "base", "small", "medium", "large"]:
        print("Invalid model. Using 'base'.")
        model_size = "base"

    try:
        recognizer = SpeechRecognizer(model_size=model_size)

        while True:
            try:
                text = recognizer.capture_audio()
                print(f"\n📝 Transcription:\n{text}")
                print(f"\n📊 Word count: {len(text.split())}")
            except (AudioCaptureError, TranscriptionError) as err:
                print(f"⚠️ Error: {err}")

            cont = input("\nPress Enter to continue or type 'quit': ").strip().lower()
            if cont in {"quit", "exit", "q"}:
                break

    except WhisperModelLoadError as err:
        print(f"❌ {err}")


if __name__ == "__main__":
    main()
