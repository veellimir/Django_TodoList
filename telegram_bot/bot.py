import asyncio

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from handlers import router
from settings.env_config import ENV__BOT_TOKEN


async def main():
    bot = Bot(token=ENV__BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
