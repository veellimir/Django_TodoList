from celery import shared_task
from django.utils.timezone import now
from apps.tasks import Task

@shared_task
def notify_due_tasks():
    tasks = Task.objects.filter(due_date__lte=now())
    for task in tasks:
        user = task.user
        if user.telegram_id:
            print(f"Notify {user.telegram_id} about task: {task.title}")
            # Здесь можно интегрировать отправку через бота
