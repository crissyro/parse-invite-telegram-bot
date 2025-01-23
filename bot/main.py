import asyncio
from aiogram import Dispatcher
from config.config import config
from handlers.start import register_start_handler
from handlers.parsing import register_parsing_handlers
from handlers.inviting import register_inviting_handlers
from utils.logger import setup_logger

async def main():
    logger = setup_logger()
    logger.info("Starting bot...")
    dp = Dispatcher(storage=config.storage)
    
    register_start_handler(dp)
    register_parsing_handlers(dp)
    register_inviting_handlers(dp)
    
    await dp.start_polling(config.bot)

if __name__ == "__main__":
    asyncio.run(main())