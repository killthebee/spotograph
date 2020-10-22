from django.urls import path

from apihand.views import SpotDetail

app_name = "apihand"


urlpatterns = [
   path('detail/', SpotDetail.as_view()),
]