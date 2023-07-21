import openai
import pinecone
import os

# OpenAI and Pinecone setup
openai.api_key = os.getenv('OPENAI_API_KEY')
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment='asia-northeast1-gcp')

class ChatService:
    @staticmethod
    def generate_response(user_input):
        # Use GPT-3.5 Turbo to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        return response

class PineconeService:
    @staticmethod
    def store_interaction(username, response):
        # Store the interaction in Pinecone
        interaction_id = pinecone.insert(items={username: response['choices'][0]['message']['content']})
        return interaction_id
