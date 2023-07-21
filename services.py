import openai
import pinecone
from config import OPENAI_API_KEY, PINECONE_API_KEY

openai.api_key = OPENAI_API_KEY
pinecone.init(api_key=PINECONE_API_KEY, environment='asia-northeast1-gcp')

def chat_service(user_input: str):
    # Use GPT-3.5 Turbo to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )
    return response
