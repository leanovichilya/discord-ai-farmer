### dispatcher.py
import random

CHANNELS = [
    "https://discord.com/channels/1234567890/0987654321",
    "https://discord.com/channels/2345678901/8765432109",
    # добавь свои
]

def get_random_channel():
    return random.choice(CHANNELS)
