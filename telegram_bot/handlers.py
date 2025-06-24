from aiogram import Router, types
from api import get_tasks

router = Router()


@router.message(commands=["tasks"])
async def list_tasks(message: types.Message):
    tasks = await get_tasks(message.from_user.id)
    if not tasks:
        await message.answer("У вас нет задач.")
        return
    response = "\n\n".join(
        [f"📌 {t['title']} (Категория: {t['category']}, Создана: {t['created_at']})" for t in tasks]
    )
    await message.answer(response)
