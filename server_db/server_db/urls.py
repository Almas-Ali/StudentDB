from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/', include('core.urls')),
    path('', views.index, name='index')
]
