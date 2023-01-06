from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase, SortableTabularInline

from .models import Place, Image


class ImageInline(SortableTabularInline):
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
class AdminPlace(SortableAdminBase, admin.ModelAdmin):
    list_display = [
        'title',
    ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class AdminImage(SortableAdminMixin, admin.ModelAdmin):
    fields = (
        'place',
        # ('place', 'position'),
        'get_preview',
        'image',
    )
    list_display = [
        'position',
        'get_preview',
        'place',
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
