from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


# Модель Клиент сервиса
class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=255, verbose_name='Full name', **NULLABLE)
    comment = models.TextField(blank=True, null=True, verbose_name='Comment')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


# Модель рассылки
class MailingMessage(models.Model):
    FREQUENCY_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )
    FIRST_CHOICES = (
        ('1', 'закончить'),
        ('2', 'сохранить'),
        ('3', 'запустить'),
    )

    subject = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    send_time = models.TimeField(verbose_name='Send time', )
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    status = models.CharField(choices=FIRST_CHOICES, verbose_name='Status',
                              default='3')
    client = models.ManyToManyField(Client, verbose_name='Clients')

    def __str__(self):
        return f"{self.body}"

    # def get_next_time_run(self) -> datetime:
    #     """Return next time run"""
    #     now = timezone.now()
    #     if self.send_time >= now.time():
    #         # Если время отправки больше или равно текущему времени сейчас, отправляем сегодня
    #         next_datetime = now.today()
    #     else:
    #         # Иначе отправляем завтра
    #         next_datetime = now.today() + timedelta(days=1)
    #
    #         # Далее добавляем интервал в зависимости от выбранной периодичности
    #         if self.frequency == 'daily':
    #             pass  # Оставляем без изменений, так как уже учтено в вычислениях выше
    #         elif self.frequency == 'weekly':
    #             next_datetime += timedelta(weeks=1)
    #         elif self.frequency == 'monthly':
    #             next_datetime += timedelta(days=30)  # Простое добавление дней
    #
    #         # Объединяем полученное дату и время отправки, чтобы получить полное время отправки
    #         next_time_run = datetime.combine(next_datetime, self.send_time)
    #

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


# Модель логов
class Log(models.Model):
    STATUS_SUCCESSFUL = 'SUCCESS'
    STATUS_FAILED = 'FAILED'

    STATUS_CHOICES = (
        (STATUS_SUCCESSFUL, 'Success'),
        (STATUS_FAILED, 'Failed'),
    )

    log_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time', **NULLABLE, )
    log_status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Status', **NULLABLE)
    log_client = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='Client', **NULLABLE, )
    log_mailing = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='Mailing', **NULLABLE, )
    log_server_response = models.TextField(**NULLABLE, verbose_name='Server response', )

    def __str__(self):
        return f"{self.log_client} - {self.log_status}"

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
