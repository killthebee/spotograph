from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from apihand.serializer import SpotDetailSerializer
from apihand.services import fetch_imgs_files
from spots.models import Spot, MainImage, FeatureImage


class SpotDetail(APIView):
    """
    Change or create spot info
    """
    def post(self, request):
        main_image, secondary_imgs = fetch_imgs_files(request.data['main'], request.data['imgs'])

        serializer = SpotDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

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

        for index, image in enumerate(secondary_imgs):
            feature_image = FeatureImage.objects.create(place=new_spot)
            feature_image.image.save(f"{index}_{serializer.validated_data['title']}.jpg", main_image, save=True)
        return Response({})