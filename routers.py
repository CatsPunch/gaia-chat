from fastapi import APIRouter, Depends
from .dependencies import get_current_active_user
from .schemas import User

router = APIRouter()

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Your code for the /token endpoint goes here

@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.post("/chat/")
@limiter.limit("5/minute")
async def chat_endpoint(user_input: str, user: User = Depends(get_current_active_user)):
    # Your code for the /chat/ endpoint goes here
