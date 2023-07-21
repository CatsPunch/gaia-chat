from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import crud, models, schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_active_user(token: str = Depends(oauth2_scheme)):
    # Your code to get the current active user goes here
