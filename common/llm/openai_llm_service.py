from common.llm.llm_service import LLMService
from openai import AsyncOpenAI

class OpenAILLMService(LLMService):
    def __init__(self, api_key: str, model:str):
        self.model = model
        self.client = AsyncOpenAI(api_key = api_key)

    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model = self.model,
            messages = [
                {
                    "role":"user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content