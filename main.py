import os
from dotenv import load_dotenv
from pymongo import MongoClient
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot.handlers import start_bot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client.get_database('task_bot_db')

def main():
    token = TELEGRAM_BOT_TOKEN
    if not token:
        raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")
    start_bot(token)

if __name__ == "__main__":
    main()
