from agent.graph import make_graph
from langchain_core.messages import HumanMessage, SystemMessage

state = {
    "user_id": 1,
    "budget": None,
    "balance": None,
    "day_of_week": 4,
    "messages": [
        SystemMessage(content="Ты помощник по управлению бюджетом. Отвечай на русском."),
        HumanMessage(content="Установи бюджет 5000"),
    ],
    "tool_call": None,
    "response": None,
}

result = make_graph(1).invoke(state)
print(result["messages"][-1].content)
