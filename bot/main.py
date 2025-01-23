from aiogram import Dispatcher, executor
from config.config import config
from handlers.start import register_handlers_start
from handlers.parsing import register_handlers_parsing
from handlers.inviting import register_handlers_inviting


def main():
    dp = Dispatcher(config.bot, storage=config.storage)
    
    register_handlers_start(dp)
    register_handlers_parsing(dp)
    register_handlers_inviting(dp)
    
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()