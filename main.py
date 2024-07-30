import os
from dotenv import load_dotenv
from pymongo import MongoClient
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot.handlers import start_bot
import requests

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client.get_database('task_bot_db')

def set_webhook():
    URL = "https://task-rlo12occo-byte-work-solution.vercel.app"
    webhook_url = f"{URL}{TELEGRAM_BOT_TOKEN}"
    response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook?url={webhook_url}")
    print(response.json())

def main():
    token = TELEGRAM_BOT_TOKEN
    if not token:
        raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")
    start_bot(token)

if __name__ == "__main__":
    set_webhook()
    main()
