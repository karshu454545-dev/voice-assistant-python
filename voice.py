import speech_recognition as sr
import webbrowser
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak command...")
    audio = r.listen(source)

command = r.recognize_google(audio)
print("You said:", command)

command = command.lower()

if "youtube" in command:
    webbrowser.open("https://youtube.com")

elif "google" in command:
    webbrowser.open("https://google.com")

elif "notepad" in command:
    os.system("notepad")

else:
    print("Command not recognized")