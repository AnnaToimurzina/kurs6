from django.db import models


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

    ADDITIONAL_STATUS_CHOICES = (
        ('pending', 'Ожидает'),
        ('processing', 'В процессе'),
        ('completed', 'Завершено'),
        ('failed', 'Не удалось'),
    )

    subject = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    send_time = models.TimeField(verbose_name='Send time', )
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    status = models.CharField(choices=FIRST_CHOICES, verbose_name='Status',default='3')
    additional_status = models.CharField(max_length=20, choices=ADDITIONAL_STATUS_CHOICES, default='pending')
    client = models.ManyToManyField(Client, verbose_name='Clients')

    def __str__(self):
        return f"{self.body}"


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
