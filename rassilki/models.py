from django.db import models
from django.contrib.auth.models import User

# Модель Клиент сервиса
class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



# Модель Рассылка
class MailingMessage(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    FREQUENCY_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    send_time = models.TimeField(default='00:00')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    status = models.CharField(max_length=20, default='created')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.body}"


