from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('playlist/', views.playlist , name='playlist'),
    path('favorite/', views.favorite , name='fav'),
    path('login/', views.login , name='login'),
    path('popular_artist/', views.popular_artist , name='popart'),
]
