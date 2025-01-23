import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

def setup_logger():
    # Создаем директорию для логов
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Конфигурация логгера
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Форматтер
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Файловый обработчик
    file_handler = RotatingFileHandler(
        filename=f"{log_dir}/bot.log",
        maxBytes=5*1024*1024,
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    # Консольный обработчик
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Добавляем обработчики
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Инициализируем глобальный логгер
logger = setup_logger()