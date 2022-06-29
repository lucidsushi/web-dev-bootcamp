from django.urls import path
from .views import spotifyTokenExists, getSpotifyAuthURL, redirect_from_spotify_auth

urlpatterns = [
    path("spotify-token-exists", spotifyTokenExists.as_view()),
    path("get-spotify-auth-url", getSpotifyAuthURL.as_view()),
    path("redirect", redirect_from_spotify_auth),
]
