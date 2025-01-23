from aiogram.fsm.state import State, StatesGroup

class ParsingStates(StatesGroup):
    source_chat = State()
    target_chat = State()