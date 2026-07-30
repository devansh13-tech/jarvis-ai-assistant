import pyttsx3
import datetime


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