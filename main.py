import pyttsx3
import datetime
import sounddevice as sd
import soundfile as sf
import webbrowser
from faster_whisper import WhisperModel


# Load Whisper model
model = WhisperModel(
    "small",
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

        sample_rate = 16000

        audio = sd.rec(
            int(seconds * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
            device=1
        )

        sd.wait()

        sf.write(filename, audio, sample_rate)

        print("✅ Recording finished.")

    except Exception as error:
        print("❌ Recording failed.")
        print(error)


def transcribe_audio(filename):
    try:
        print("🎙️ Transcribing audio...")

        segments, info = model.transcribe(
            filename,
            language="en",
            beam_size=5
        )

        print(f"Language   : {info.language}")
        print(f"Confidence : {info.language_probability:.2f}")

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()

    except Exception as error:
        print("❌ Transcription failed.")
        print(error)
        return ""


def listen():
    record_audio(5, "assets/output.wav")
    text = transcribe_audio("assets/output.wav")
    return text


def process_command(command):
    command = command.lower()

    if "hello" in command:
        speak("Hello Devansh")

    elif "who are you" in command or "your name" in command:
        speak("I am Jarvis, your personal AI assistant.")

    elif "how are you" in command:
        speak("I am fine. Thank you for asking.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")

    elif "google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "exit" in command or "shutdown" in command:
        speak("Goodbye! Have a great day ahead.")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True


# ---------------- MAIN ---------------- #

start_jarvis()

while True:

    wake_word = listen()

    print("\nYou said:")
    print(repr(wake_word))
    print(wake_word.lower())

    print("Checking wake word...")

    if "jarvis" in wake_word.lower():

        print("Wake word detected!")

        speak("Yes?")

        command = listen()

        print("\nCommand:")
        print(command)

        running = process_command(command)

        if not running:
            break