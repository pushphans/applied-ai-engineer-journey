from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    session_id: str = Field(
        ..., description="A unique identifier for the user's session."
    )
    user_input: str = Field(
        ..., description="The input provided by the user for processing."
    )
