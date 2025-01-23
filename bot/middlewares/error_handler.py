from aiogram import types
from config.config import config

async def error_middleware(update, error):
    await config.bot.send_message(
        config.ADMIN_ID,
        f"An error occurred: {str(error)}"
    )
    return True