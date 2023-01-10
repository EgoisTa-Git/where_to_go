from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=150,
    )
    description_short = models.TextField(
        'Краткое описание',
        blank=True,
    )
    description_long = HTMLField(
        'Описание',
        blank=True,
    )
    lng = models.FloatField(
        'Долгота',
    )
    lat = models.FloatField(
        'Широта',
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(
        'Картинка',
    )
    position = models.IntegerField(
        'Позиция',
        default=0,
        db_index=True,
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images',
    )

    class Meta:
        ordering = (
            'position',
        )

    def __str__(self):
        return self.place.title
