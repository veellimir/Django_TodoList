from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from telegram_bot.states import AddTaskStates
from telegram_bot.api import add_task


async def on_title_input(m, dialog_manager, **_):
    dialog_manager.dialog_data["title"] = m.text
    await dialog_manager.next()


async def on_due_date_input(m, dialog_manager, **_):
    title = dialog_manager.dialog_data["title"]
    category = "some-category-id"  # Можно выбрать через кнопки
    due_date = m.text
    telegram_id = m.from_user.id
    await add_task(telegram_id, title, category, due_date)
    await dialog_manager.done()


add_task_dialog = Dialog(
    Window(
        Const("Введите название задачи"),
        MessageInput(on_title_input),
        state=AddTaskStates.title,
    ),
    Window(
        Const("Введите дату исполнения (в формате YYYY-MM-DD HH:MM)"),
        MessageInput(on_due_date_input),
        state=AddTaskStates.due_date,
    )
)
