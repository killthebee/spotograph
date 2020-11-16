from django.urls import path

from chat import views


app_name = 'chat'

urlpatterns = [
    path('<int:spot_id>/', views.spot_chat_room, name='spot_chat')
]