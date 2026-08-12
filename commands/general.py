from core.speaker import speak
import datetime


def handle_general_command(command):
    if "hello" in command:
        speak("Hello Devansh")
        return True

    elif "who are you" in command or "your name" in command:
        speak("I am Jarvis, your personal AI assistant.")
        return True

    elif "how are you" in command:
        speak("I am fine. Thank you for asking.")
        return True

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return True

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")
        return True

    return False