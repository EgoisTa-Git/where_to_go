from django.utils.html import format_html


def get_html_preview(place):
    return format_html(
        '<img src="{url}" height={height}/>',
        url=place.image.url,
        height=200,
    )
