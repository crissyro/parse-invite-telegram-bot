import os
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()

class Config:
    API_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    
    bot = Bot(token=API_TOKEN)
    storage = MemoryStorage()

config = Config()