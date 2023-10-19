# import pytz
# import os
#
# import django
# from django.core.mail import send_mail
# from rassilki.models import MailingMessage
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()
#
# first = MailingMessage.objects.all()
# print(first)
#
# all_timezones = pytz.all_timezones
# print(all_timezones)
#
#
# def send_mailing(mailing):
#     subject = mailing.subject
#     message = mailing.body
#     print(subject)
#     print(message)
#
#     recipient_list = ['ariadna.kamenetskaya@yandex.ru']
#
#     send_mail(subject, message, '2402as@gmail.com', recipient_list)
#
#
# send_mailing(first[1])
