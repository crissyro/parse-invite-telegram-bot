import os
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.ADMIN_ID = int(os.getenv("ADMIN_ID"))
        self.API_ID = int(os.getenv("API_ID"))
        self.API_HASH = os.getenv("API_HASH")
        self.storage = MemoryStorage()
        self.bot = Bot(token=self.BOT_TOKEN)
        
        if not self.BOT_TOKEN or not self.ADMIN_ID or not self.API_ID or not self.API_HASH:
            raise ValueError("Environment variables not set")

config = Config()
