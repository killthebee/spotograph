from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class SpotDetail(APIView):
    """
    Change or create spot info
    """
    def post(self, request):
        print(request.data)
        return Response({})