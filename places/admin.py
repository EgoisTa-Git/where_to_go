from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = [
        'get_preview',
    ]

    def get_preview(self, obj):
        return format_html(
            '<img src="{url}" height={height}/>',
            url=obj.image.url,
            height=100,
        )


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
    fields = (
        ('place', 'position'),
        'get_preview',
        'image',
    )
    list_editable = [
        'position',
    ]
    list_display = [
        'place',
        'get_preview',
        'position',
    ]
    list_filter = [
        'place'
    ]
    readonly_fields = [
        'get_preview',
    ]

    def get_preview(self, obj):
        return format_html(
            '<img src="{url}" height={height}/>',
            url=obj.image.url,
            height=200,
        )
