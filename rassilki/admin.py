from django.contrib import admin
from .models import Client, MailingMessage, Log



admin.site.register(Client)
admin.site.register(Log)



@admin.register(MailingMessage)
class MailingMessageAdmin (admin.ModelAdmin):
    list_display = ('id', 'body', 'status',)
    list_filter = ('status', 'client')
    search_fields = ('body', 'status', 'client')