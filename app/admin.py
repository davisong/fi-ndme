from django.contrib import admin

from .models import PhoneCall, TextMessage

# Register your models here.

admin.site.register(PhoneCall)
admin.site.register(TextMessage)
