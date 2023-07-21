import openai
from ..models import ChatInput, ChatResponse
from ..core.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def chat(user, user_input):
    # Use GPT-3.5 Turbo to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )

    # Return the response
    return ChatResponse(response=response['choices'][0]['message']['content'])

