import subprocess
from core.speaker import speak


def open_application(command, name):
    try:
        speak(f"Opening {name}.")
        subprocess.Popen(command)
        return True

    except Exception as error:
        print(f"❌ Failed to open {name}.")
        print(error)
        speak(f"Sorry, I couldn't open {name}.")
        return False


def handle_system_command(command):
    if "open notepad" in command:
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

    else:
        return False

    return True