def detect_intent(command):
    command = command.lower().strip()
    words = command.split()

    if any(word in words for word in ["open", "launch", "start"]):
        return {
            "intent": "open",
            "command": command
        }

    if any(word in words for word in ["search", "google", "find"]):
        return {
            "intent": "search",
            "command": command
        }

    if any(word in words for word in ["play", "music", "song"]):
        return {
            "intent": "play",
            "command": command
        }

    if any(word in words for word in ["time", "date"]):
        return {
            "intent": "time",
            "command": command
        }

    return {
        "intent": "unknown",
        "command": command
    }


if __name__ == "__main__":
    print(detect_intent("open youtube"))
    print(detect_intent("search for python"))
    print(detect_intent("play music"))
    print(detect_intent("what time is it"))
    print(detect_intent("explain artificial intelligence"))