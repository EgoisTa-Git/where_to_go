from django.db import models


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=150,
    )
    description_short = models.CharField(
        'Краткое описание',
        max_length=250,
    )
    description_long = models.TextField(
        'Описание',
        blank=True,
    )
    lng_coordinate = models.DecimalField(
        'Долгота',
        max_digits=16,
        decimal_places=14,
    )
    lat_coordinate = models.DecimalField(
        'Широта',
        max_digits=16,
        decimal_places=14,
    )
