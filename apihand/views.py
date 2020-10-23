from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from apihand.serializer import SpotDetailSerializer
from spots.models import Spot

class SpotDetail(APIView):
    """
    Change or create spot info
    """
    def post(self, request):
        print('request')
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
        return Response({})