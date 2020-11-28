from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.template import loader
from django.urls import reverse
from django.urls import reverse_lazy

from spots.models import Spot, MainImage, FeatureImage
from spots.forms import SignUpForm
from chat.services import serialize_messages


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
    try:
        context['user_spots'] = request.user.spots.all()
    except AttributeError:
        context['user_spots'] = None

    return render(request, 'index.html', context)


def fetch_spot_details(request, pk):
    """
    Fetch json with spot details
    """
    spot = get_object_or_404(Spot, pk=pk)
    imgs = [image.image.url for image in spot.images.all()]
    imgs.insert(0, spot.main_image.main_image.url)
    coords = {"lat": spot.latitude, "lng": spot.longitude}
    messages = serialize_messages(spot.messages.order_by('-time').all()[:3])
    details = {
        "title": spot.title,
        "imgs": imgs,
        "description_short": spot.description,
        "description_long": spot.features,
        "coordinates": coords,
        'vk_link': spot.vk,
        'inst_link': spot.inst,
        'messages': messages,
    }
    return JsonResponse(details, safe=False, json_dumps_params={'ensure_ascii': False})


def show_cms(request, pk):
    context = {'new': 'new'}
    try:
        owned_spots = request.user.spots.all()
        if pk > 0:
            spot = get_object_or_404(Spot, pk=pk)
            if spot in owned_spots:
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
    except AttributeError:
        return redirect('login')
    try:
        context['user_spots'] = request.user.spots.all()
    except AttributeError:
        context['user_spots'] = None
    return render(request, 'cms.html', context)


class SpotLoginView(LoginView):
    template_name = 'login.html'


class SpotLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('signup_done')


class RegisterDoneView(TemplateView):
    template_name = 'signup_done.html'