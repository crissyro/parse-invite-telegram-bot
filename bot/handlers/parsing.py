from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from aiogram import types
from aiogram.filters import Command
from services.csv_manager import save_members_to_csv
from config.config import config


async def cmd_parse(message: types.Message):
    await message.reply("Отправьте @username канала, чтобы начать парсинг:")

async def process_parse(message: types.Message):
    try:
        chat_username = message.text
        await message.reply("Начинаем парсинг пользователей...")

        async with TelegramClient('session', config.API_ID, config.API_HASH) as client:
            members = []
            async for user in client.iter_participants(chat_username):
                if user.username:
                    members.append((user.id, user.username))
            
            await save_members_to_csv(members)
            await message.reply(f"✅ Парсинг завершен! Собрано {len(members)} пользователей.")
    except FloodWaitError as e:
        await message.reply(f"❌ Telegram временно заблокировал запросы. Подождите {e.seconds} секунд.")
    except Exception as e:
        await message.reply(f"❌ Ошибка: {str(e)}")

def register_parsing_handlers(dp):
    dp.message.register(cmd_parse, Command("parse"))
    dp.message.register(process_parse)
