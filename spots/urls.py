from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_page),
    path('cms/', views.show_cms),
]