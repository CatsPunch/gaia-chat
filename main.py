from fastapi import FastAPI
from app.routers import chatbot, users

app = FastAPI()

app.include_router(chatbot.router)
app.include_router(users.router)
