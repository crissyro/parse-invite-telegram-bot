from aiogram import types
from aiogram.filters import Command


async def cmd_start(message: types.Message):
    await message.reply(
        "🤖 Бот для управления участниками:\n\n"
        "🔍 /parse - собрать пользователей из канала\n"
        "📨 /invite - пригласить пользователей из CSV в канал\n\n"
        "⚠️ Убедитесь, что бот имеет все необходимые права в обоих каналах!"
    )

def register_start_handler(dp):
    dp.message.register(cmd_start, Command("start"))
