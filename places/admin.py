from django.contrib import admin
from .models import Place


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = [
        'title',
    ]
