from config.settings import Settings
from agents.ragagent.rag_agent import RagAgent
from common.llm.llm_factory import LLMFactory

settings = Settings()
# print("settings", settings.LLM_PROVIDER, settings.OPENAI_API_KEY, settings.OPENAI_MODEL)

#asking llmservice to provide llm to pass it to agent 
if settings.LLM_PROVIDER == "openai":
    llm_Service = LLMFactory.get_llm(
        provider=settings.LLM_PROVIDER,
        config={
            "api_key": settings.OPENAI_API_KEY,
            "model": settings.OPENAI_MODEL
        }
    )
elif settings.LLM_PROVIDER == "gemini":
    llm_Service = LLMFactory.get_llm(
        provider=settings.LLM_PROVIDER,
        config={
            "api_key": settings.GEMINI_API_KEY,
            "model": settings.GEMINI_MODEL
        }
    )
else:
    raise ValueError("Unsupported Provider")

#injecting llm to agent
rag_agent = RagAgent(
    llm_service=llm_Service
)