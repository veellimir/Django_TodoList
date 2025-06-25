from aiogram import Bot

from settings import env_config

bot = Bot(token=env_config.ENV__BOT_TOKEN)


async def send_telegram_message(telegram_id: int, text: str):
    try:
        await bot.send_message(
            chat_id=telegram_id,
            text=text,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"❌ Ошибка отправки сообщения пользователю {telegram_id}: {e}")
