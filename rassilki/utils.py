import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.core.mail import send_mail
from rassilki.models import MailingMessage


def send_mailing(mailing):
    subject = mailing.subject
    message = mailing.body
    recipient_list = ['ariadna.kamenetskaya@yandex.ru']

    send_mail(subject, message, '2402as@gmail.com', recipient_list)

send_mailing(MailingMessage)