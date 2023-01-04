from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_editable = [
        'position',
    ]
    list_display = [
        'place',
        'position',
    ]
    list_filter = [
        'place'
    ]
