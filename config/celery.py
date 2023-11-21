import os
from celery import Celery
from celery.schedules import crontab

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Автоматически обнаруживать и регистрировать задачи приложений Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка настроек из файла Django
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_mailing': {
        'task': 'rassilki.tasks.send_mails',
        'schedule': crontab(minute='1'),
    },
}








