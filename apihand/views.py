from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.base import ContentFile
from urllib import request as rq

from apihand.serializer import SpotDetailSerializer
from spots.models import Spot, MainImage


class SpotDetail(APIView):
    """
    Change or create spot info
    """
    def post(self, request):
        try:
            with rq.urlopen(request.data['main']) as response:
                data = response.read()
                main_image = ContentFile(data)
        except:
            pass

        serializer = SpotDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data['title'])
        new_spot = Spot.objects.create(
            title=serializer.validated_data['title'],
            description=serializer.validated_data['description'],
            features=serializer.validated_data['features'],
            latitude=serializer.validated_data['latitude'],
            longitude=serializer.validated_data['longitude'],
            inst=serializer.validated_data['inst'],
            vk=serializer.validated_data['vk'],
        )
        new_main_image = MainImage.objects.create(spot=new_spot)
        new_main_image.main_image.save('lel222.jpg', main_image, save=True)
        return Response({})