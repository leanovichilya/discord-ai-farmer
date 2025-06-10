### message_gen.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_message(context: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты участник крипто-коммьюнити, обсуждаешь DeFi, Layer 2, фарм, мемы и т.п."},
            {"role": "user", "content": f"Придумай сообщение для Discord: {context}"}
        ],
        temperature=0.9
    )
    return response.choices[0].message.content.strip()