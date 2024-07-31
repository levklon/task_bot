import os
from dotenv import load_dotenv
from pymongo import MongoClient
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot.handlers import start_bot
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client.get_database('task_bot_db')

app = FastAPI()

def set_webhook():
    URL = "https://task-ee43pyvgy-byte-work-solution.vercel.app"
    webhook_url = f"{URL}/{TELEGRAM_BOT_TOKEN}"
    response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook?url={webhook_url}")
    print(response.json())

@app.on_event("startup")
async def startup_event():
    set_webhook()
    token = TELEGRAM_BOT_TOKEN
    if not token:
        raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")
    start_bot(token)

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Task Bot is running!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
