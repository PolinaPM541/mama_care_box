from fastapi import APIRouter

from app.config import settings
from app.user.auth import cookie_backend, fastapi_users
from app.user.oauth import facebook_oauth_client, google_oauth_client
from app.user.schemas import UserCreate, UserRead, UserUpdate

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(cookie_backend), prefix="/auth/cookie", tags=["auth"]
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
router.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        cookie_backend,
        settings.SECRETS,
        redirect_url="http://127.0.0.1:8000/",
    ),
    prefix="/auth/google",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_oauth_router(
        facebook_oauth_client,
        cookie_backend,
        settings.SECRETS,
        redirect_url="http://localhost:8000/auth/facebook/callback",
    ),
    prefix="/auth/facebook",
    tags=["auth"],
)
