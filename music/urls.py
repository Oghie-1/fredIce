from django.urls import path
from . import views


urlpatterns = [
    path("", views.albumlist, name="album_list"),
    path("", views.songList, name="songList")
]