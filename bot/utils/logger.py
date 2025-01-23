import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

def setup_logger():

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{log_dir}/bot_{date_str}.log"
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=5*1024*1024,  
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger