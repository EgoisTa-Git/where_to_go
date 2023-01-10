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
                    place.lng,
                    place.lat,
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
    return render(request, 'places/index.html', context={'places': collection})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    content = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.order_by('position')],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }
    return JsonResponse(content, safe=True)
