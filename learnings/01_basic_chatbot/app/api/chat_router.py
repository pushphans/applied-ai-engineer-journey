from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.chat_request import chat_request
from app.chatbot_agent.basic_chatbot_graph import workflow
from langchain.messages import HumanMessage, AIMessage, SystemMessage


chat_router = APIRouter(prefix="/api/v1")


@chat_router.post("/chat")
async def chat(request: chat_request):

    async def generate_chat():
        config = {"configurable": {"thread_id": request.thread_id}}
        async for chunk in workflow.astream(
            {"messages": [HumanMessage(content=request.message)]},
            config=config,
            stream_mode="messages",
        ):
            if chunk[0].content:
                yield chunk[0].content

    return StreamingResponse(generate_chat(), media_type="text/plain")
