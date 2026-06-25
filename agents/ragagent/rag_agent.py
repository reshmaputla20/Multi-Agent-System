from typing import Dict, Any
from common.base_agent import BaseAgent

class RagAgent(BaseAgent):
    def __init__(self, llm_service, retriever):
        self.llm_service = llm_service
        self.retriever = retriever

    async def execute(self, payload : Dict[str, Any]) -> Dict[str, Any]:
        
        query = payload["query"]
        context = self.retriever.get_context(query)

        prompt = f"""

        Context: {context}
        Question: {query}
        You are a helpfull assistant helping users by answering their queries, using the provided context 
        """
        answer = await self.llm_service.generate(prompt)
        return {
            "query":query,
            "answer": answer,
            "context": context
        }
    
    async def health_check(self):
        return {
            "agent":"rag_agent",
            "status":"healthy"
        }

