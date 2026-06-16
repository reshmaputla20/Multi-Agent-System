from typing import Dict, Any
from common.base_agent import BaseAgent

class RagAgent(BaseAgent):
    def __init__(self, llm_service):
        self.llm_service = llm_service

    async def execute(self, payload : Dict[str, Any]) -> Dict[str, Any]:
        context = payload["context"]
        query = payload["query"]

        prompt = f"""

        Context: {context}
        Question: {query}
        Answer the question only using the provided context 
        """
        answer = await self.llm_service.generate(prompt)
        return {
            "answer": answer,
            "context": context
        }
    
    async def health_check(self):
        return {
            "agent":"raga_agent",
            "status":"healthy"
        }

