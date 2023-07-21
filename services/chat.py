import openai
import logging
from ..models import ChatInput, ChatResponse
from ..core.config import settings
from fastapi import HTTPException

openai.api_key = settings.OPENAI_API_KEY

logger = logging.getLogger(__name__)

async def chat(user, user_input):
    try:
        # Use GPT-3.5 Turbo to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )

        # Log the response
        logger.info(f"Generated response for user {user.username}")

        # Return the response
        return ChatResponse(response=response['choices'][0]['message']['content'])

    except Exception as e:
        logger.error(f"An error occurred while generating a response: {e}")
        raise HTTPException(status_code=500, detail="An error occurred. Please try again later.")
