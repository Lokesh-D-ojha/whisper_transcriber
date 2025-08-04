# Whisper Transcriber CLI 🎤

A minimalist, robust command-line tool that brings the power of **OpenAI's Whisper** to your terminal for high-accuracy, local speech-to-text transcription.

This project uses `sounddevice` for microphone input, eliminating the need for `PyAudio` and its complex installation.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

---

## ✨ Key Features

*   **🔒 Local & Private**: Your audio never leaves your machine. No cloud APIs, no privacy concerns.
*   **🎯 High Accuracy**: Leverage the full power of Whisper's models, from `tiny` to `large`.
*   **🎧 PyAudio-Free**: Uses `sounddevice` for smoother installation and reliable microphone access.
*   **⚙️ Simple & Robust**: A clean command-line interface with clear error handling for a seamless experience.
*   **🪟 Windows Ready**: Pre-configured to find `ffmpeg` on Windows, solving common setup issues.

---

## 🚀 Demo

Here's what it looks like in action:

```text
┌───────────────────────────────────────────────────┐
│ [whisper_transcriber] - C:\Windows\System32\cmd.exe │
└───────────────────────────────────────────────────┘

> python main.py

🎤 Whisper Transcriber CLI
========================================
Enter model size (tiny/base/small/medium/large): base
Loading Whisper model 'base'...
Model 'base' loaded successfully.

Press Enter to continue or type 'quit':
Recording audio for 5 seconds... Speak now!
Temporary audio file saved: C:\Users\lojha\AppData\Local\Temp\tmp20w13tds.wav
Temporary file kept at: C:\Users\lojha\AppData\Local\Temp\tmp20w13tds.wav

📝 Transcription:
Hello, this is a test of the Whisper transcriber, and it seems to be working perfectly.

📊 Word count: 15

Press Enter to continue or type 'quit': quit


##  🛠️ Installation & Setup
Get up and running in three simple steps.

Prerequisites: Python 3.8+, Git, and a microphone.

1. Install ffmpeg (Crucial Requirement)
Whisper needs ffmpeg to process audio. The script is hard-coded to find it in a specific location on Windows.

Download the essentials build from Gyan.dev's FFmpeg Builds.
Extract the archive to C:\ffmpeg. The script will automatically find it there.
2. Clone the Repository
Open your terminal and run the following command:

Bash

git clone https://github.com/your-username/whisper_transcriber.git
3. Install Python Dependencies
Navigate into the project folder and install the required packages
You are now ready to run the application

## 📂 Project Structure
.
├── main.py             # CLI entry point and user interface loop
├── recognizer.py       # Core class for audio capture & transcription
├── exceptions.py       # Custom exception classes
├── logger_config.py    # Logging configuration
├── requirements.txt    # Python package dependencies
└── README.md           # You are here!
