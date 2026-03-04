from aiogram.types import Message
from agent.graph import graph
from langchain_core.messages import HumanMessage
import re


def answer_agent(user_id, user_messages):

    state = {
        "user_id": user_id,
        "budget": None,
        "balance": None,
        "day_of_week": 0,
        "messages": [HumanMessage(content=user_messages)],
        "tool_call": None,
        "response": None,
    }

    answer = graph.invoke(state)
    text = answer["messages"][-1].content
    clean_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL, count=1)
    return clean_text.strip()




