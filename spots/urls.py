from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_page, name='index'),
    path('spotdetails/<int:pk>/', views.fetch_spot_details, name='details'),
    path('cms/<int:pk>', views.show_cms, name='cms'),
    path('accounts/login/', views.SpotLoginView.as_view(), name='login'),
    path('accounts/logout/', views.SpotLogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.RegisterUserView.as_view(), name='signup'),
    path('accounts/signupdone/', views.RegisterDoneView.as_view(), name='signup_done'),
]