from pydantic import BaseModel, Field


class travel_request(BaseModel):
    message: str = Field(..., description="User's message for travel plan")
