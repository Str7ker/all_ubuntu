from django.contrib import admin
from .models import Confirmation

class ConfirmationAdmin(admin.ModelAdmin):
    list_display = ('email', 'viber', 'sms')
admin.site.register(Confirmation,ConfirmationAdmin)

# admin.site.register(Confirmation)