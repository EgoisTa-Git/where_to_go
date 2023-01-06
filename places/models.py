from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=150,
    )
    description_short = models.TextField(
        'Краткое описание',
    )
    description_long = HTMLField(
        'Описание',
        blank=True,
    )
    lng_coordinate = models.FloatField(
        'Долгота',
    )
    lat_coordinate = models.FloatField(
        'Широта',
    )

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

    def __str__(self):
        return f'{self.position} {self.place}'

    class Meta:
        ordering = (
            'position',
        )
