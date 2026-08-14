class ConversationContext:
    def __init__(self):
        self.last_command = ""
        self.last_response = ""

    def update(self, command, response=""):
        self.last_command = command
        self.last_response = response

    def get_last_command(self):
        return self.last_command

    def get_last_response(self):
        return self.last_response

    def clear(self):
        self.last_command = ""
        self.last_response = ""

conversation_history = []


def add_message(role, content):
    conversation_history.append({
        "role": role,
        "content": content
    })


def get_history():
    return conversation_history


def clear_history():
    conversation_history.clear()