from httpx_oauth.clients.facebook import FacebookOAuth2
from httpx_oauth.clients.google import GoogleOAuth2

from app.config import settings

facebook_oauth_client = FacebookOAuth2(
    client_id=settings.FACEBOOK_OAUTH2_CLIENT_ID,
    client_secret=settings.FACEBOOK_OAUTH2_CLIENT_SECRET,
    scopes=["email"],
)


google_oauth_client = GoogleOAuth2(
    client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
    client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
    scopes=[
        "openid",
        "email",
        "profile",
    ],
)
