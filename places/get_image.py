from django.utils.html import format_html


def get_html_preview(obj):
    return format_html(
        '<img src="{url}" height={height}/>',
        url=obj.image.url,
        height=200,
    )
