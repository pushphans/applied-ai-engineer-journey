from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    user_input: str = Field(..., description="The user's input to the agent")
