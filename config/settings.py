import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):

        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.OPENAI_MODEL = os.getenv("OPENAI_MODEL")
        self.LLM_PROVIDER = os.getenv(
                "LLM_PROVIDER"
        )
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.GEMINI_MODEL = os.getenv("GEMINI_MODEL")

