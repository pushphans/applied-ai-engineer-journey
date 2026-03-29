from typing import TypedDict, Annotated
from langgraph.graph.message import AnyMessage, add_messages


class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
