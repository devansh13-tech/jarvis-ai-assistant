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
                    "You are Jarvis, an intelligent personal AI assistant. "
                    "You speak naturally and briefly because your responses are read aloud. "
                    "You are friendly, practical, and conversational. "
                    "Use previous conversation context when helpful. "
                    "Keep normal answers to 2 or 3 short sentences unless the user asks for more detail. "
                    "If asked about coding, explain clearly and simply. "
                    "Never describe your reasoning or analyze the user's message. "
                    "Just give the final answer."
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