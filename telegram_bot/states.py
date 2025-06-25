from aiogram.fsm.state import StatesGroup, State


class AddTaskStates(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()
    waiting_for_category = State()
    waiting_for_username = State()
    waiting_for_due_date = State()
