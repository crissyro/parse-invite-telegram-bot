from aiogram import types
from aiogram.filters import Command
from config.config import config

async def cmd_start(message: types.Message):
    await message.reply(
        "🤖 Бот для управления участниками\n"
        "➖➖➖➖➖➖➖➖➖➖\n"
        "🔍 /parse - собрать пользователей\n"
        "📨 /invite - пригласить пользователей\n"
        "➖➖➖➖➖➖➖➖➖➖\n"
        "⚙️ Бот должен быть админом в обоих чатах!"
    )

def register_start_handler(dp):
    dp.message.register(cmd_start, Command("start"))