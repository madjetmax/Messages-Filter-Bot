from aiogram.fsm.state import State, StatesGroup

class AdminTriggersSetting(StatesGroup):
    add_keywords = State()
    add_trigger_names = State()
    add_phrases = State()

class MessagesClear(StatesGroup):
    messages_to_delete = State() # list[int]