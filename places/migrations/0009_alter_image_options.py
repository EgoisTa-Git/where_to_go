# Generated by Django 4.1.5 on 2023-01-06 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('position',)},
        ),
    ]
