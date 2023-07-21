from fastapi import APIRouter, Depends
from ..services import chat as chat_service
from ..schemas import ChatInput, ChatResponse
from ..core.auth import get_current_active_user

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(chat_input: ChatInput, user = Depends(get_current_active_user)):
    response = await chat_service.chat(user, chat_input.user_input)
    return response
