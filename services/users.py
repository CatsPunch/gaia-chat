from ..models import User, UserInDB
from ..core.config import settings
from ..core.auth import get_password_hash, verify_password, create_access_token
from datetime import timedelta

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_user(username: str):
    if username in settings.fake_users_db:
        user_dict = settings.fake_users_db[username]
        return UserInDB(**user_dict)

def create_access_token_for_user(user: UserInDB):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return access_token
