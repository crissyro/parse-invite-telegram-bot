from aiogram import types
from config.config import config
from states.parsing_states import ParsingStates
from services.csv_manager import read_members_from_csv
from services.chat_operations import invite_users

async def cmd_invite(message: types.Message):
    await ParsingStates.target_chat.set()
    await message.reply("Send target chat ID:")

async def process_target_chat(message: types.Message):
    try:
        target_chat = await config.bot.get_chat(message.text)
        members = read_members_from_csv()
        result = await invite_users(target_chat.id, members)
        await message.reply(result)
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

def register_handlers_inviting(dp):
    dp.register_message_handler(cmd_invite, commands=['invite'], state=None)
    dp.register_message_handler(process_target_chat, state=ParsingStates.target_chat)