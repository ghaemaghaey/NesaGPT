from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Balance)
admin.site.register(models.Memory)
admin.site.register(models.ChatMessage)
admin.site.register(models.ChatSession)
admin.site.register(models.Profile)
