from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    agent_response: str = Field(
        ..., description="The agent's response to the user's input"
    )
