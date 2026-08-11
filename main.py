import pyttsx3
import datetime
import sounddevice as sd
import soundfile as sf
import webbrowser
import subprocess
from faster_whisper import WhisperModel



model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

AUDIO_FILE = "assets/output.wav"
RECORD_SECONDS = 5

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


def search_google(query):
    speak(f"Searching for {query}.")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def open_website(url, name):
    speak(f"Opening {name}.")
    webbrowser.open(url)

def open_application(command, name):
    speak(f"Opening {name}.")
    subprocess.Popen(command)

def unknown_command(command):
    speak(f"Sorry, I don't understand the command: {command}.")



def process_command(command):
    command = clean_command(command)

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

    elif "search" in command:
            query = command.replace("search", "").strip()
    
            if query.startswith("for "):
                query = query.replace("for ", "", 1).strip()
    
            if query == "":
                speak("What can I search for?")
            else:
                search_google(query)

    elif "google" in command:
        query = command.replace("google", "").strip()
        query = query.replace("open", "").strip()

        if query == "":
            open_website("https://www.google.com", "Google")
        else:
            search_google(query)

    elif "youtube" in command:
        query = command.replace("youtube", "").strip()
        query = query.replace("open", "").strip()

        if query == "":
            open_website("https://www.youtube.com", "YouTube")
        else:
            speak(f"Searching YouTube for {query}.")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

    elif "github" in command:
        query = command.replace("github", "").strip()
        query = query.replace("open", "").strip()

        if query == "":
            open_website("https://github.com", "GitHub")
        else:
            speak(f"Searching GitHub for {query}.")
            webbrowser.open(
                f"https://github.com/search?q={query}"
            )

    elif "open notepad" in command:
        open_application("notepad", "Notepad")

    elif "open calculator" in command:
        open_application("calc", "Calculator")

    elif "open explorer" in command or "open file explorer" in command:
        open_application("explorer", "File Explorer")

    elif "open command prompt" in command or "open cmd" in command:
        open_application("cmd", "Command Prompt")

    elif "open paint" in command:
        open_application("mspaint", "Paint")

    elif "open code" in command or "open visual studio code" in command:
        open_application("code", "Visual Studio Code")

    


    elif command in ["exit", "shutdown", "quit", "goodbye"]:
        speak("Goodbye! Have a great day ahead.")
        return False

    elif "help" in command:
        speak("I can open websites, search Google, search YouTube, search GitHub, open Windows applications, tell you the time and date, and answer basic questions.")

    else:
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