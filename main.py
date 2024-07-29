import os
from dotenv import load_dotenv

load_dotenv()

print("TELEGRAM_BOT_TOKEN:", os.getenv("TELEGRAM_BOT_TOKEN"))
print("MONGODB_URI:", os.getenv("MONGODB_URI"))

from bot.handlers import start_bot

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")
    start_bot(token)

if __name__ == "__main__":
    main()
