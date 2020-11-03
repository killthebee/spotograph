from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse

from spots.models import Spot, MainImage, FeatureImage


def show_page(request):
    """
    fetch spots geo data
    """
    spots = Spot.objects.all()
    features = []
    for spot in spots:
        coordinates = [spot.longitude, spot.latitude]
        title = spot.title
        place_id = spot.pk

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coordinates,
            },
            "properties": {
                "title": title,
                "placeId": place_id,
                "detailsUrl": reverse('details', kwargs={'pk': place_id})
            },
        }
        features.append(feature)

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {"places_geojson": places_geojson}
    return render(request, 'index.html', context)


def fetch_spot_details(request, pk):
    """
    Fetch json with spot details
    """
    spot = get_object_or_404(Spot, pk=pk)
    imgs = [image.image.url for image in spot.images.all()]
    imgs.insert(0, spot.main_image.main_image.url)
    coords = {"lat": spot.latitude, "lng": spot.longitude}
    details = {
        "title": spot.title,
        "imgs": imgs,
        "description_short": spot.description,
        "description_long": spot.features,
        "coordinates": coords,
    }
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False})


def show_cms(request, pk):
    context = {'new': 'new'}
    if pk > 0:
        spot = get_object_or_404(Spot, pk=pk)
        context = {
            'title': spot.title,
            'description': spot.description,
            'features': spot.features,
            'latitude': spot.latitude,
            'longitude': spot.longitude,
            'inst': spot.inst,
            'vk': spot.vk,
            'main_image': spot.main_image.main_image,
            'features_images': spot.images.all()
        }
    return render(request, 'cms.html', context)