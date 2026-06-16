from google import genai
from common.llm.llm_service import LLMService

class GeminiLLMService(LLMService):
    def __init__(self, api_key: str, model: str):
        self.model = model
        self.client = genai.Client(api_key=api_key)
    async def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model= self.model,
            contents=prompt

        )
        return response.text

