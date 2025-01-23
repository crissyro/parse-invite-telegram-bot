from aiogram import types
from aiogram.fsm.context import FSMContext
from config.config import config
from states.parsing_states import ParsingStates
from services.csv_manager import save_members_to_csv
from aiogram.filters import Command
from utils.logger import logger
import asyncio

async def cmd_parse(message: types.Message, state: FSMContext):
    await state.set_state(ParsingStates.source_chat)
    await message.reply("Отправьте ID или @username исходного чата:")

async def process_source_chat(message: types.Message, state: FSMContext):
    try:
        chat = await config.bot.get_chat(message.text)
        total_members = await config.bot.get_chat_member_count(chat.id)
        await message.reply(f"Начат парсинг {total_members} пользователей...")

        members = []
        count = 0
        async for member in config.bot.get_chat_members(chat.id):
            user = member.user
            if user.username:
                members.append((user.id, user.username))
                count += 1
                
                if len(members) >= 100:
                    await save_members_to_csv(members)
                    members.clear()
                    await asyncio.sleep(1)

        if members:
            await save_members_to_csv(members)

        await message.reply(f"✅ Парсинг завершен! Собрано {count} пользователей")
        await state.clear()

    except Exception as e:
        logger.error(f"Ошибка парсинга: {str(e)}", exc_info=True)
        await message.reply(f"❌ Ошибка: {str(e)}")
        await state.clear()

def register_parsing_handlers(dp):
    dp.message.register(cmd_parse, Command("parse"))
    dp.message.register(process_source_chat, ParsingStates.source_chat)