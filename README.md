# 🎙️ VoiceMate — Voice Assistant in Python

A Python-based voice-controlled assistant that listens to spoken commands and automates tasks like opening websites, apps, and more.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

## 📸 About the Project
VoiceMate is a voice command automation tool built in Python. It uses speech recognition to listen to the user's voice and executes actions like opening YouTube, launching the camera, and responding with text-to-speech — all hands-free.

## ✨ Features
- 🎤 Listens to voice commands in real time using the microphone
- 🌐 Opens websites like YouTube, Google, etc. on voice command
- 📷 Launches the system camera on command
- 🗣️ Responds with spoken feedback using text-to-speech
- 🤖 Handles unrecognized commands gracefully

## 🛠️ Technologies Used
| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `speech_recognition` | Captures and converts voice to text |
| `pyttsx3` | Text-to-speech engine for responses |
| `webbrowser` | Opens URLs in the default browser |
| `subprocess` | Launches system applications |
| Jupyter Notebook | Development and testing environment |

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/karshu454545-dev/voice-assistant-python.git
   cd voice-assistant-python
   ```

2. Install required libraries:
   ```bash
   pip install speechrecognition pyttsx3 pyaudio
   ```

3. Run the notebook:
   - Open `voice_assistant.ipynb` in Jupyter Notebook
   - Run all cells and speak into your microphone when prompted

## 🗣️ Example Voice Commands
| Command | Action |
|---|---|
| "Open YouTube" | Opens YouTube in the browser |
| "Open camera" | Launches the system camera |
| "Open Google" | Opens Google in the browser |

## 🎯 What I Learned
- Working with Python libraries for real-world automation
- Using `speech_recognition` to capture live microphone input
- Implementing text-to-speech responses with `pyttsx3`
- Handling exceptions and edge cases in voice input
- Automating system-level tasks using Python

## 👩‍💻 Author
**Karishma Shaik**
- GitHub: [@karshu454545-dev](https://github.com/karshu454545-dev)
- LinkedIn: [Karishma Shaik](https://www.linkedin.com/in/karishma-shaik-g2707)
