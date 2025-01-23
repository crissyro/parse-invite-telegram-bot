from aiogram import types
from config.config import config

async def cmd_start(message: types.Message):
    await message.reply(
        "Hi! I'm a bot for managing chat participants.\n"
        "Use /parse to collect users\n"
        "Use /invite to invite users"
    )

def register_handlers_start(dp):
    dp.register_message_handler(cmd_start, commands=['start'])