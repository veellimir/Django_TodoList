import asyncio

from celery import shared_task
from django.utils.timezone import now

from apps.tasks.models import Task
from telegram_bot.notifications import send_telegram_message


def send_telegram_message_sync(telegram_id, text):
    # Синхронная фн-ция для решения конфликта при вызове send_telegram_message
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if loop.is_running():
        raise RuntimeError("Event loop уже запущен, невозможно вызвать синхронно")
    return loop.run_until_complete(send_telegram_message(telegram_id, text))


@shared_task
def notify_due_tasks():
    tasks = Task.objects.filter(due_date__lte=now())
    for task in tasks:
        user = task.user
        if user.telegram_id:
            text = (
                f"⏰ Внимания ! У вас deadline по задаче!\n\n"
                f"📌 *{task.title}*\n"
                f"📅 Дата завершения: {task.due_date.strftime('%Y-%m-%d')}"
            )
            try:
                send_telegram_message_sync(user.telegram_id, text)
            except Exception as e:
                print(f"❌ Ошибка при отправке в Telegram: {e}")

    """В идеале можно повесить флаг в модель и отслеживать его, 
    чтобы не присылать каждый раз напоминания по конкретной задачи !"""
