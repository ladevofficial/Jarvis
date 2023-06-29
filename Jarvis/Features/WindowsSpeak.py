import pyttsx3
import pyaudio

engine = pyttsx3.init()

def say(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()