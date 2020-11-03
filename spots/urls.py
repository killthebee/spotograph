from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_page),
    path('spotdetails/<int:pk>/', views.fetch_spot_details, name='details'),
    path('cms/<int:pk>', views.show_cms),
]