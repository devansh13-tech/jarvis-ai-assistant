import webbrowser
from core.speaker import speak


def search_google(query):
    speak(f"Searching for {query}.")
    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )


def open_website(url, name):
    speak(f"Opening {name}.")
    webbrowser.open(url)


def search_youtube(query):
    speak(f"Searching YouTube for {query}.")
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )


def search_github(query):
    speak(f"Searching GitHub for {query}.")
    webbrowser.open(
        f"https://github.com/search?q={query}"
    )

def handle_web_command(command):
    if "search" in command:
        query = command.replace("search", "").strip()

        if query.startswith("for "):
            query = query.replace("for ", "", 1).strip()

        if query == "":
            speak("What can I search for?")
        else:
            search_google(query)

        return True

    elif "google" in command:
        query = command.replace("google", "").strip()
        query = query.replace("open", "").strip()

        if query == "":
            open_website("https://www.google.com", "Google")
        else:
            search_google(query)

        return True

    elif "youtube" in command:
        query = command.replace("youtube", "").strip()
        query = query.replace("open", "").strip()

        if query == "":
            open_website("https://www.youtube.com", "YouTube")
        else:
            search_youtube(query)

        return True

    elif "github" in command:
        query = command.replace("github", "").strip()
        query = query.replace("open", "").strip()

        if query == "":
            open_website("https://github.com", "GitHub")
        else:
            search_github(query)

        return True

    return False