from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("/parse"), KeyboardButton("/invite")]
        ],
        resize_keyboard=True
    )