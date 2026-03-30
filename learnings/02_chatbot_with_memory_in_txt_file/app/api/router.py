from fastapi import APIRouter, HTTPException
from app.models.request_model import RequestModel
from app.models.response_model import ResponseModel
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from app.core.connection_pool import connection_pool, checkpointer
from app.agent.chatbot_with_memory.chatbot_graph import graph
from app.core.agent_state import AgentState
from langchain.messages import HumanMessage


router = APIRouter(prefix="/api/v1")


@router.post("/chat")
async def chat(request: RequestModel):
    try:
        # step1 : graph ko checkpointer ke sath compile karo
        app = graph.compile(checkpointer=checkpointer)       # checkponiter banaya hai connection_pool.py mein to keep router and main.py clean

        # step2 : graph ko execute karo with initial state
        config = {"configurable": {"thread_id": request.session_id}}

        initial_state: AgentState = {
            "messages": [HumanMessage(content=request.user_input)]
        }

        final_state: AgentState = await app.ainvoke(initial_state, config=config)

        return ResponseModel(response=final_state["messages"][-1].content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
