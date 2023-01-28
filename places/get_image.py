from django.utils.html import format_html


def get_html_preview(image):
    return format_html(
        '<img src="{url}" height={height}/>',
        url=image.image.url,
        height=200,
    )
