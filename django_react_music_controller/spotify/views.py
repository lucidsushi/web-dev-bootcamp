from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from requests import Request, post

from .credentials import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET
from .models import SpotifyToken


class spotifyTokenExists(APIView):
    """check if token exists and needs refresh -- user a session id"""

    def get(self, request, format=None):
        user_token = get_user_token(self.request.session.session_key)
        if user_token:
            user_is_authenticated = True
            if not is_spotify_token_fresh(user_token):
                refresh_spotify_token(user_token)
        else:
            user_is_authenticated = False

        return Response({"status": user_is_authenticated}, status=status.HTTP_200_OK)


class getSpotifyAuthURL(APIView):
    """return a url to request login at Spotify"""

    def get(self, request, format=None):
        scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
        # https://github.com/psf/requests/blob/main/requests/models.py#L230
        url = (
            Request(
                "GET",
                "https://accounts.spotify.com/authorize",
                params={
                    "scope": scopes,
                    "response_type": "code",
                    "redirect_uri": REDIRECT_URI,
                    "client_id": CLIENT_ID,
                },
            )
            .prepare()
            .url
        )

        return Response({"url": url}, status=status.HTTP_200_OK)


def redirect_from_spotify_auth(request):
    """
    - provide spotify an endpoint to redirect to after auth (login)
    - associated session_id as user, and store token model in db
    """
    code = request.GET.get("code")
    # error = request.GET.get("error")

    token_response = post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    ).json()
    # error = token_response.get("error")

    create_session_if_missing(request)
    update_or_create_user_token(token_response, session_id=request.session.session_key)

    return redirect(
        "frontend:"
    )  # HttpResponse  named in frontend.urls -- required return


def get_user_token(session_id):
    user_tokens = SpotifyToken.objects.filter(user=session_id)
    if user_tokens.exists():
        # list(SpotifyToken.objects.all().values_list("user", flat=True))
        return user_tokens[0]
    else:
        print("token doesnt exist for session -- what im scared of", session_id)
        return None


def is_spotify_token_fresh(token):
    expiry = token.expires_in
    if expiry <= timezone.now():
        # print("existing token expired, please refresh token")
        return False
    else:
        # print("existing token is fresh")
        return True


def refresh_spotify_token(token):
    token_response = post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": token.refresh_token,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    ).json()

    update_or_create_user_token(token_response, token)


def update_or_create_user_token(token_response, token="", session_id=""):
    access_token = token_response.get("access_token")
    token_type = token_response.get("token_type")
    refresh_token = token_response.get("refresh_token")
    expires_in = timezone.now() + timedelta(
        seconds=token_response.get("expires_in")
    )  # expires_in (timezone) != expires_in (seconds)

    # update token
    if token:
        token.access_token = access_token
        token.token_type = token_type
        token.refresh_token = refresh_token
        token.expires_in = expires_in
        token.save(
            update_fields=["access_token", "refresh_token", "expires_in", "token_type"]
        )
    # create token
    else:
        token = SpotifyToken(
            user=session_id,
            access_token=access_token,
            token_type=token_type,
            refresh_token=refresh_token,
            expires_in=expires_in,
        )
        token.save()


def create_session_if_missing(request):
    # django request
    # https://github.com/encode/django-rest-framework/blob/master/rest_framework/views.py#L493
    if not request.session.exists(request.session.session_key):
        request.session.create()
    return request  #  does this solve the unique key bug?
