from django.contrib import admin

from rassilki.models import MailingMessage, Client, Log

'''admin.site.register(Client)
admin.site.register(MailingMessage)'''

@admin.register(Client)
class ClientAdmin (admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment')
    search_fields = ('email',)

@admin.register(MailingMessage)
class MailingMessageAdmin (admin.ModelAdmin):
    list_display = ('body', 'status', 'client')
    list_filter = ('status', 'client')
    search_fields = ('body', 'status', 'client')


@admin.register(Log)
class LogMessageAdmin(admin.ModelAdmin):
    list_display = ('STATUS_CHOICES', 'log_client', 'log_created_at', 'log_mailing', 'log_status', 'log_server_response')
    search_fields = ('log_status', 'log_client', 'log_mailing')



