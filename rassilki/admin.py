from django.contrib import admin

from rassilki.models import MailingMessage, Client

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

