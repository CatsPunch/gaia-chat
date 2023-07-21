import os
from dotenv import load_dotenv
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse

# Import routers
from routers import chatbot, users

# Load environment variables
load_dotenv()

# FastAPI and security setup
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(HTTPException, _rate_limit_exceeded_handler)

# Include routers
app.include_router(chatbot.router)
app.include_router(users.router)

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    logging.error(f"An error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content="An error occurred. Please try again later.",
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
