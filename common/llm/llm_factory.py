from common.llm.openai_llm_service import OpenAILLMService
from common.llm.gemini_ai_service import GeminiLLMService

class LLMFactory:
    @staticmethod
    def get_llm(provider, config):
        if provider == "openai":
            # print("7", config)


            return OpenAILLMService(
                api_key=config["api_key"],
                model = config["model"]
            )
        elif provider == "gemini":
            return GeminiLLMService(
                api_key= config["api_key"],
                model = config["model"]
            )
        raise ValueError(f"Unsuported provider: {provider}")