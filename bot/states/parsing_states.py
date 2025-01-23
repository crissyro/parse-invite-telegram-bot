from aiogram.dispatcher.filters.state import State, StatesGroup

class ParsingStates(StatesGroup):
    source_chat = State()
    target_chat = State()