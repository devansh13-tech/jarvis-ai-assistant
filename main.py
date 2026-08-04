import pyttsx3
import datetime
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
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


def start_jarvis():
    speak("Starting Jarvis.")
    wish()
    speak("How can I help you?")


def record_audio(seconds, filename):
    try:
        print("🎤 Recording... Speak now!")

        sample_rate = 44100

        audio = sd.rec(
            seconds * sample_rate,
            samplerate=sample_rate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(filename, audio, sample_rate)

        print("✅ Recording finished.")

    except Exception as error:
        print("❌ Recording failed.")
        print(error)


def transcribe_audio(filename):
    try:
        print(" Transcribing audio...")

        segments, info = model.transcribe(filename)

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()

    except Exception as error:
        print(" Transcription failed.")
        print(error)
        return ""

def listen():
    record_audio(5, "output.wav")

    text = transcribe_audio("output.wav")

    return text

start_jarvis()

while True:
    wake_word = listen()

    print("\nYou said:")
    print(repr(wake_word))
    print(wake_word.lower())

    print("Checking wake word...")

    if "hey jarvis" in wake_word.lower():
        print("Wake word detected!")

        speak("Yes?")

        command = listen()

        command = listen()

        print("Command:")
        print(command)

    