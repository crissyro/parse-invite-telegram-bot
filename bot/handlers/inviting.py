from aiogram import types
from aiogram.filters import Command
from services.csv_manager import read_members_from_csv
from config.config import config
import asyncio


async def cmd_invite(message: types.Message):
    await message.reply("Отправьте @username или ID целевого канала для приглашения:")

async def process_invite(message: types.Message):
    try:
        target_chat = message.text
        members = await read_members_from_csv()

        await message.reply(f"Начинаем приглашение {len(members)} пользователей...")
        success, failed = 0, 0

        for i, (user_id, username) in enumerate(members, start=1):
            try:
                await config.bot.add_chat_members(chat_id=target_chat, user_ids=[user_id])
                success += 1
            except Exception as e:
                failed += 1

            await asyncio.sleep(2)  # Задержка между запросами

        await message.reply(
            f"✅ Приглашение завершено!\n"
            f"Успешно: {success}\n"
            f"Ошибок: {failed}"
        )
    except Exception as e:
        await message.reply(f"❌ Ошибка: {str(e)}")

def register_inviting_handlers(dp):
    dp.message.register(cmd_invite, Command("invite"))
    dp.message.register(process_invite)
