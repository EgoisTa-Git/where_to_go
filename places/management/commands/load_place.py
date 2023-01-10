import json

import requests
from pathlib import Path

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Add new point to map'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json',
            type=Path,
            required=True,
            help='Path to JSON file',
        )
        parser.add_argument(
            '--skip_imgs',
            action='store_true',
            help='Skip uploading images',
        )

    def handle(self, *args, **options):
        json_path = Path.joinpath(settings.BASE_DIR, options['json'])
        if json_path.suffix != '.json':
            raise CommandError('Wrong file type, JSON needed!')
        if not Path.exists(json_path):
            raise CommandError('File not found!')
        with open(json_path, 'r') as file:
            json_place = json.load(file)
        Place.objects.get_or_create(
            title=json_place['title'],
            description_short=json_place['description_short'],
            description_long=json_place['description_long'],
            lng=json_place['coordinates']['lng'],
            lat=json_place['coordinates']['lat'],
        )
        self.stdout.write(
            self.style.SUCCESS(f"Place {json_place['title']} created!")
        )
        if not options['skip_imgs']:
            place = Place.objects.get(title=json_place['title'])
            existing_images = [
                Path(image.image.url).name for image in place.images.all()
            ]
            for image_url in json_place['imgs']:
                image_path = Path(image_url)
                if image_path.name not in existing_images:
                    img = Image()
                    serialized_image = requests.get(image_url).content
                    img.place = place
                    img.position = json_place['imgs'].index(image_url)
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(serialized_image)
                    img_temp.flush()
                    img.image.save(image_path.name, File(img_temp))
                    img.save()
                    self.stdout.write(
                        self.style.SUCCESS(f"Image {image_path.name} saved!")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Image {image_path.name} exists!")
                    )
                    continue
