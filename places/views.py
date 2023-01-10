from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Place


def index(request):
    serialized_places = []
    for place in Place.objects.all():
        place = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    place.lng_coordinate,
                    place.lat_coordinate,
                ]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': f'places/{place.pk}/'
            }
        }
        serialized_places.append(place)
    collection = {'type': 'FeatureCollection', 'features': serialized_places}
    return render(request, 'places/index.html', context={'data': collection})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all().order_by('position')
    image_urls = []
    for image in images:
        image_urls.append(image.image.url)
    content = {
        'title': place.title,
        'imgs': image_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat_coordinate,
            'lng': place.lng_coordinate,
        },
    }
    return JsonResponse(content, safe=True)
