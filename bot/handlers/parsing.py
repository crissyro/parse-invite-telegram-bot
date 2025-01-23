from aiogram import types
from config.config import config
from states.parsing_states import ParsingStates
from services.csv_manager import save_members_to_csv

async def cmd_parse(message: types.Message):
    await ParsingStates.source_chat.set()
    await message.reply("Send chat ID or @username for parsing:")

async def process_source_chat(message: types.Message):
    try:
        chat = await config.bot.get_chat(message.text)
        members = []
        
        async for member in config.bot.get_chat_members(chat.id):
            user = member.user
            if user.username:
                members.append((user.id, user.username))
        
        save_members_to_csv(members)
        await message.reply(f"Collected {len(members)} users")

    except Exception as e:
        await message.reply(f"Error: {str(e)}")

def register_handlers_parsing(dp):
    dp.register_message_handler(cmd_parse, commands=['parse'], state=None)
    dp.register_message_handler(process_source_chat, state=ParsingStates.source_chat)