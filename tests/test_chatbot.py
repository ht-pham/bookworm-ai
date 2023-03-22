import pytest
from app.chatbot import Chatbot

@pytest.fixture
def ai_engine():
    yield Chatbot()

def test_introduce(ai_engine):
    expected = ai_engine.introduce()
    assert "BookwormAI" in expected
    assert "an AI created by OpenAI" in expected
    assert "a book title" in expected

def test_autoreply(ai_engine):
    expected = ai_engine.autoReply()
    assert "another" in expected 