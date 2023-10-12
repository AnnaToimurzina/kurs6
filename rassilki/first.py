

from django.core.mail import send_mail

from config import settings


def send():
    send_mail(
        subject= 'test',
        message='test_body',
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=['2402as@gmail.com'],
        fail_silently=False,
    )

if __name__== '__main__':
        send()