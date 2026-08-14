from dotenv import load_dotenv
from openai import OpenAI
from core.context import add_message, get_history
import os

load_dotenv()

api_key = os.getenv("AI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(prompt):
    try:
        add_message("user", prompt)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a helpful voice assistant. "
                    "Keep your responses concise and natural for speech."
                )
            }
        ]

        messages.extend(get_history())

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages
        )

        ai_response = response.choices[0].message.content.strip()

        add_message("assistant", ai_response)

        return ai_response

    except Exception as error:
        print("❌ AI request failed.")
        print(error)

        return "Sorry, I am having trouble connecting to my AI brain."