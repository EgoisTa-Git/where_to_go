import json
from hashlib import md5

import requests
from pathlib import Path
from urllib.parse import urlparse

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from places.models import Place, Image


def json_url(raw_url):
    url = urlparse(raw_url)
    if all((url.scheme, url.netloc)):
        return raw_url
    raise CommandError('Invalid URL')


def create_place(json_place):
    try:
        place, created = Place.objects.get_or_create(
            lng=json_place['coordinates']['lng'],
            lat=json_place['coordinates']['lat'],
            defaults={
                'title': json_place['title'],
                'description_short': json_place.get('description_short', ''),
                'description_long': json_place.get('description_long', ''),
            },
        )
    except KeyError:
        raise CommandError(
            'No required fields found! Use JSON format from README.md!'
        )
    return place, created


def add_images(obj, json_place, place):
    try:
        json_place['imgs']
    except KeyError:
        obj.stdout.write(
            obj.style.WARNING('No images found!')
        )
        return
    for position, image_url in enumerate(json_place['imgs']):
        image_content = requests.get(image_url).content
        image_name = md5(image_content).hexdigest() + Path(image_url).suffix
        content_file = ContentFile(
            image_content,
            name=image_name,
        )
        Image.objects.create(
            place=place,
            image=content_file,
            position=position,
        )
        obj.stdout.write(
            obj.style.SUCCESS(f'Image {image_name} saved!')
        )


class Command(BaseCommand):
    help = 'Add new point to map'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=Path,
            help='Path to JSON file',
        )
        parser.add_argument(
            '--url',
            type=json_url,
            help='URL to JSON file',
        )
        parser.add_argument(
            '--skip_imgs',
            action='store_true',
            help='Skip uploading images',
        )

    def handle(self, *args, **options):
        if options['file'] and options['url']:
            raise CommandError(
                'Both arguments("url" and "file") are specified. Choose one!'
            )

        if not (options['file'] or options['url']):
            raise CommandError('No action requested. Add argument!')

        if options['file']:
            json_path = Path.joinpath(settings.BASE_DIR, options['file'])
            if not Path.exists(json_path):
                raise CommandError('File not found!')
            with open(json_path, 'r') as file:
                try:
                    json_place = json.load(file)
                except json.JSONDecodeError:
                    raise CommandError('Wrong file type, JSON needed!')

        if options['url']:
            response = requests.get(options['url'])
            response.raise_for_status()
            json_place = response.json()

        place, created = create_place(json_place)
        if not created:
            self.stdout.write(
                self.style.WARNING(f'{json_place["title"]} already exists!')
            )
            return

        self.stdout.write(
            self.style.SUCCESS(f'Place {json_place["title"]} created!')
        )
        if not options['skip_imgs']:
            add_images(self, json_place, place)
