from fastapi import APIRouter, HTTPException
from app.models.request_model import RequestModel
from app.models.response_model import ResponseModel
from app.agents.basic_bot.basic_bot_graph import app
from app.core.agent_state import AgentState
from langchain.messages import HumanMessage

router = APIRouter(prefix="/api/v1")


@router.post("/ask-bot")
async def ask_bot(request: RequestModel):
    try:

        initial_state: AgentState = {
            "messages": [HumanMessage(content=request.user_input)]
        }

        response: AgentState = await app.ainvoke(initial_state)

        return ResponseModel(agent_response=response["messages"][-1].content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect: {str(e)}")
