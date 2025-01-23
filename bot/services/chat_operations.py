import logging
from config.config import config
import asyncio

logger = logging.getLogger(__name__)

async def invite_users(chat_id: int, members: list) -> str:
    success = 0
    failed = 0
    
    for member in members:
        try:
            await config.bot.add_chat_member(
                chat_id=chat_id,
                user_id=int(member[0])
            )
            success += 1
            await asyncio.sleep(5)
        except Exception as e:
            failed += 1
            logger.error(f"Invite error: {str(e)}")
    
    return f"Успешно: {success}, Ошибок: {failed}"