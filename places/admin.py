from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin

from .get_image import get_html_preview
from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = [
        'get_preview',
    ]

    @staticmethod
    def get_preview(obj):
        return get_html_preview(obj)


@admin.register(Place)
class AdminPlace(SortableAdminBase, admin.ModelAdmin):
    search_fields = [
        'title',
    ]
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

    @staticmethod
    def get_preview(obj):
        return get_html_preview(obj)
