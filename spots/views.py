from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from spots.models import Spot
def show_page(request):
    context = {}
    return render(request, 'index.html', context)


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