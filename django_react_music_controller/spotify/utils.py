from datetime import timedelta

from django.utils import timezone
from requests import post, put, get

from .models import SpotifyToken
from .credentials import CLIENT_ID, CLIENT_SECRET


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
