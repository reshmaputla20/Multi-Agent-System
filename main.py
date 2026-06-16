from fastapi import FastAPI
from startup import rag_agent

app = FastAPI()

@app.get("/health")
async def health_check():
    return await rag_agent.health_check()

@app.post("/rag_agent")
async def ragagent(payload: dict):
    print("inside")
    response = await rag_agent.execute(payload)                                             
    return response

