from generator.llm_generation import generate_tests_with_llm, build_prompt
from generator.code_analysis import FunctionInfo
from pathlib import Path
import os

class DummyResponse:
    class Choice:
        def __init__(self):
            self.message = {"content": "def test_dummy(): pass"}

    def __init__(self):
        self.choices = [self.Choice()]

class DummyClient:
    class Chat:
        class Completions:
            def create(self, **kwargs):
                return DummyResponse()
        completions = Completions()
    chat = Chat()

def test_generate_tests_with_llm(monkeypatch, tmp_path):
    # Fake API key
    monkeypatch.setenv("OPENAI_API_KEY", "fake")

    # Fake client
    monkeypatch.setattr("generator.llm_generation.OpenAI", lambda api_key: DummyClient())

    # Create dummy function info
    fn = FunctionInfo(
        name="add",
        args=["a", "b"],
        docstring="Adds two numbers",
        source="def add(a, b): return a + b"
    )

    # Run function
    result = generate_tests_with_llm(Path("dummy.py"), [fn])

    assert "test_dummy" in result
