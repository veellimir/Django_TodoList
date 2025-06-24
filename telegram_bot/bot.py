import asyncio
from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from handlers import router

from settings.env_config import ENV__BOT_TOKEN
from dialogs.add_task import add_task_dialog


async def main():
    bot = Bot(token=ENV__BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(add_task_dialog)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
