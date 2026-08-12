import datetime
import sounddevice as sd
import soundfile as sf
import webbrowser

from faster_whisper import WhisperModel
from commands.general import handle_general_command
from core.speaker import speak

from commands.system import handle_system_command

from commands.web import handle_web_command



model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

AUDIO_FILE = "assets/output.wav"
RECORD_SECONDS = 5




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
    record_audio(RECORD_SECONDS, AUDIO_FILE)
    text = transcribe_audio(AUDIO_FILE)
    return text.strip()


def clean_command(command):
    command = command.lower().strip()

    command = command.replace(".", "")
    command = command.replace("?", "")
    command = command.replace("!", "")

    if command.startswith("please "):
        command = command.replace("please ", "", 1).strip()

    return command

def unknown_command(command):
    speak(f"Sorry, I don't understand the command: {command}.")



def process_command(command):
    command = clean_command(command)

    if command in ["exit", "shutdown", "quit", "goodbye"]:
        speak("Goodbye! Have a great day ahead.")
        return False

    if "help" in command:
        speak(
            "I can open websites, search Google, search YouTube, "
            "search GitHub, open Windows applications, tell you "
            "the time and date, and answer basic questions."
        )
        return True

    handlers = [
        handle_general_command,
        handle_system_command,
        handle_web_command
    ]

    for handler in handlers:
        if handler(command):
            return True

    unknown_command(command)
    return True



start_jarvis()

while True:

    wake_word = listen()

    if not wake_word:
        continue

    wake_word = wake_word.lower()

    print("\nYou said:")
    print(repr(wake_word))
    print("Checking wake word...")

    if "jarvis" in wake_word:

        print("Wake word detected!")

        speak("Yes?")

        command = listen()

        if not command:
            speak("I didn't catch that.")
            continue

        print("\nCommand:")
        print(command)

        running = process_command(command)

        if not running:
            break