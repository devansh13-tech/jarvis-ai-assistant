import pyttsx3
import datetime
import sounddevice as sd
import soundfile as sf
import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("base",
                     device="cpu",
                     compute_type="int8"
                     )



def speak(text):
    engine = pyttsx3.init()
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def wish():
    hour = datetime.datetime.now().hour

    if hour < 5:
        speak("Good Night.")

    elif hour < 12:
        speak("Good Morning.")

    elif hour < 13:
        speak("Good Noon.")

    elif hour < 18:
        speak("Good Afternoon.")

    elif hour < 22:
        speak("Good Evening.")

    else:
        speak("Good Night.")


def start_Jarvis():

    speak("Starting Jarvis.")

    wish()

    speak("I am Jarvis.")

    speak("How can I help you?")

    speak("I am ready.")


start_Jarvis()

def record_audio(seconds, filename):
    print("Recording audio...")
    sample_rate = 44100

    audio = sd.rec(
        seconds * sample_rate,
        samplerate = sample_rate,
        channels = 1,
        dtype = "float32"
    )
    sd.wait()

    sf.write(filename, audio, sample_rate)

    print("Recording is saved successfully.")

record_audio(5, "output.wav")


def transcribe_audio(filename):
    print("Transcribing audio.......")
    segments, info = model.transcribe(filename)

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()

text = transcribe_audio("output.wav")
print(text)



