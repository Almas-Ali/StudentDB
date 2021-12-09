from django.urls import path
from core import views


urlpatterns = [
    path('', views.server_index, name='server_index'),
    path('login', views.loginX, name='login'),
]
