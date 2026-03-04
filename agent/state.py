from typing import TypedDict, Optional, List
from langchain_core.messages import BaseMessage
from typing import Annotated
import operator
from langchain_core.messages import BaseMessage


class State(TypedDict):
    """Состояние агента"""
    user_id: int
    budget: Optional[int]
    balance: Optional[int]
    day_of_week: int
    messages: Annotated[List[BaseMessage], operator.add]
    tool_call: Optional[dict]
    response: Optional[str]