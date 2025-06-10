### main.py

from message_gen import generate_message
from sender import send_message
from dispatcher import get_random_channel
import time
import random


def main():
    while True:
        channel_url = get_random_channel()
        prompt_context = "Обсуждаем крипту, Layer 2, фарм и мемы"
        message = generate_message(prompt_context)
        send_message(channel_url, message)
        sleep_time = random.uniform(120, 300)
        print(f"[✓] Sent message. Sleeping {int(sleep_time)} sec")
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()