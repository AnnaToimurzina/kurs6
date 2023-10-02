from django.core.mail import send_mail
from .models import MailingMessage
def send_mailing(mailing):
    subject = mailing.subject
    message = mailing.message
    recipient_list = mailing.recipient_list

    send_mail(subject, message, '2402as@gmail.com', recipient_list)