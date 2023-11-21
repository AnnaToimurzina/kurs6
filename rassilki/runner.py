import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE, чтобы указать на ваш файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Теперь вы можете импортировать и использовать вашу функцию send_mails
from rassilki.tasks import send_mails

# Запускайте вашу функцию
send_mails()