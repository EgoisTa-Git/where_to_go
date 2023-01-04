from django.shortcuts import render

from .models import Place


def index(request):
    serialized_places = []
    for place in Place.objects.all():
        place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.lng_coordinate,
                    place.lat_coordinate,
                ]
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": f"/static/places/{place.pk}.json"
            }
        }
        serialized_places.append(place)
    collection = {'type': 'FeatureCollection', 'features': serialized_places}
    return render(request, 'places/index.html', context={"data": collection})
