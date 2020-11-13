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

        if int(request.data['pk']) == 0:
            spot = Spot.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                features=serializer.validated_data['features'],
                latitude=serializer.validated_data['latitude'],
                longitude=serializer.validated_data['longitude'],
                inst=serializer.validated_data['inst'],
                vk=serializer.validated_data['vk'],
                owner=request.user,
            )

            new_main_image = MainImage.objects.create(spot=spot)
            new_main_image.main_image.save('lel222.jpg', main_image, save=True)

        elif int(request.data['pk']) > 0:

            pk = request.data['pk']
            Spot.objects.filter(pk=pk).update(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                features=serializer.validated_data['features'],
                latitude=serializer.validated_data['latitude'],
                longitude=serializer.validated_data['longitude'],
                inst=serializer.validated_data['inst'],
                vk=serializer.validated_data['vk'],
            )

            spot = Spot.objects.get(pk=pk)
            spot.main_image.main_image.save('lel222.jpg', main_image, save=True)
            spot.images.all().delete()

        for index, image in enumerate(secondary_imgs):
            feature_image = FeatureImage.objects.create(place=spot)
            feature_image.image.save(f"{index}_{serializer.validated_data['title']}.jpg", image, save=True)

        return Response({})