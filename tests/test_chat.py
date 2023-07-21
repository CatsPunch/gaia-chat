import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..models import ChatInput

client = TestClient(app)

def test_chat_endpoint():
    response = client.post(
        "/chat/",
        json={"user_input": "Hello, world!"},
    )
    assert response.status_code == 200
    assert "response" in response.json()
