### sender.py
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()
PROFILE_PATH = os.getenv("PROFILE_PATH")


def send_message(channel_url: str, message: str):
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(PROFILE_PATH, headless=False)
        page = browser.new_page()
        page.goto(channel_url)
        page.wait_for_selector('div[role="textbox"]', timeout=10000)
        page.click('div[role="textbox"]')
        page.keyboard.type(message)
        page.keyboard.press('Enter')
        print(f"[+] Sent: {message}")
        browser.close()