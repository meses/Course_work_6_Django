from django.contrib import admin

from mainapp.models import Client, Message, SendingStatus, Periodicty, SendingSettings, SendingLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_title', 'message_body',)

@admin.register(SendingStatus)
class SendingStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)

@admin.register(Periodicty)
class PeriodictyAdmin(admin.ModelAdmin):
    list_display = ('per_name',)

@admin.register(SendingSettings)
class SendingSettingsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'sending_time', 'periodicity_id', 'message_id', 'status_id',)

@admin.register(SendingLog)
class SendingLogAdmin(admin.ModelAdmin):
    list_display = ('recipient_id', 'attempt_time', 'attempt_status', 'server_response',)