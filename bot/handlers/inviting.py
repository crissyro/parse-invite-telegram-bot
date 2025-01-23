from aiogram import types
from aiogram.fsm.context import FSMContext
from config.config import config
from states.parsing_states import ParsingStates
from services.csv_manager import read_members_from_csv
from aiogram.filters import Command
from utils.logger import logger
import asyncio

async def cmd_invite(message: types.Message, state: FSMContext):
    await state.set_state(ParsingStates.target_chat)
    await message.reply("Отправьте ID или @username целевого чата:")

async def process_target_chat(message: types.Message, state: FSMContext):
    try:
        target_chat = await config.bot.get_chat(message.text)
        members = await read_members_from_csv()
        total = len(members)
        success = 0
        failed = 0
        
        await message.reply(f"Начато приглашение {total} пользователей...")

        for i, (user_id, username) in enumerate(members, 1):
            try:
                await config.bot.add_chat_member(
                    chat_id=target_chat.id,
                    user_id=user_id
                )
                success += 1
                
                if i % 20 == 0:
                    await message.reply(
                        f"Прогресс: {i}/{total}\n"
                        f"Успешно: {success} | Ошибок: {failed}"
                    )
                
                await asyncio.sleep(3 if i % 30 == 0 else 1)

            except Exception as e:
                failed += 1

        await message.reply(
            f"✅ Приглашение завершено!\n"
            f"Успешно: {success}\n"
            f"Ошибок: {failed}"
        )
        await state.clear()

    except Exception as e:
        logger.error(f"Ошибка приглашения: {str(e)}", exc_info=True)
        await message.reply(f"❌ Ошибка: {str(e)}")
        await state.clear()

def register_inviting_handlers(dp):
    dp.message.register(cmd_invite, Command("invite"))
    dp.message.register(process_target_chat, ParsingStates.target_chat)