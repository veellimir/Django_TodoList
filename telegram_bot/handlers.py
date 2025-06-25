from datetime import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from api import *

router = Router()


class AddTaskStates(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()
    waiting_for_category = State()
    waiting_for_username = State()
    waiting_for_due_date = State()


@router.message(F.text == "/addtask")
async def start_add_task(message: types.Message, state: FSMContext):
    await message.answer("Введите название задачи:")
    await state.set_state(AddTaskStates.waiting_for_title)


@router.message(AddTaskStates.waiting_for_title)
async def process_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Введите описание задачи:")
    await state.set_state(AddTaskStates.waiting_for_description)


@router.message(AddTaskStates.waiting_for_description)
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите название категории:")
    await state.set_state(AddTaskStates.waiting_for_category)


@router.message(AddTaskStates.waiting_for_category)
async def process_category(message: types.Message, state: FSMContext):
    category_name = message.text
    category = await get_category_by_name(category_name)
    if not category:
        await message.answer(
            f"❌ Категория '{category_name}' не найдена. "
            f"Пожалуйста, введите название категории заново:"
        )
        return
    await state.update_data(category_name=category_name)
    await message.answer("Введите username пользователя:")
    await state.set_state(AddTaskStates.waiting_for_username)


@router.message(AddTaskStates.waiting_for_username)
async def process_username(message: types.Message, state: FSMContext):
    username = message.text
    user = await get_user_by_username(username)
    if not user:
        await message.answer(
            f"❌ Пользователь с username '{username}' не найден. "
            f"Пожалуйста, введите username заново:"
        )
        return
    await state.update_data(username=username)
    await message.answer("Введите срок выполнения в формате ГГГГ-ММ-ДД:")
    await state.set_state(AddTaskStates.waiting_for_due_date)


@router.message(AddTaskStates.waiting_for_due_date)
async def process_due_date(message: types.Message, state: FSMContext):
    due_date_str = message.text
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        due_date_iso = due_date.isoformat()
    except ValueError:
        await message.answer(
            "❌ Неверный формат даты. Пожалуйста, "
            "введите дату заново (ГГГГ-ММ-ДД):"
        )
        return

    data = await state.get_data()
    title = data.get('title')
    description = data.get('description')
    category_name = data.get('category_name')
    username = data.get('username')

    success = await add_task(title, description, due_date_iso, username, category_name)

    if success:
        await message.answer(f"✅ Задача '{title}' успешно создана.")
    else:
        await message.answer("❌ Ошибка при создании задачи. Попробуйте позже.")
    await state.clear()


@router.message(F.text == "/tasks")
async def list_tasks(message: types.Message):
    tasks = await get_tasks(message.from_user.id)

    if not tasks:
        await message.answer("У вас нет задач.")
        return
    response = "\n\n".join(
        [f"📌 {t['title']}\nКатегория: {t['category']}, \nСоздана: {t['created_at']})" for t in tasks]
    )
    await message.answer(response)
