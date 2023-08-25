# Django
from django.urls import path

# Local
from .views import (
    DetailView,
    IndexView,
    create_song
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:album_id>/', DetailView.as_view(), name='detail'),
    path('<int:song_id>/', create_song, name='create_song')
]
