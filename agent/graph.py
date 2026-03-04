from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.messages import SystemMessage

from agent.state import State
from agent.llm import llm
from agent.tools import set_budget, get_balance, generate_menu, recalculate, create_order


llm_with_tools = llm.bind_tools([set_budget, get_balance, generate_menu, recalculate, create_order])


def agent_node(state: State) -> dict:

    messages = state["messages"]

    response = llm_with_tools.invoke(messages)

    return {"messages": [response]}


def should_continue(state: State) -> str:
    """
    Проверяем, есть ли tool_call в ответе LLM.
    Если да → идём в tools_node.
    Если нет → завершаем (END).
    """
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END


builder = StateGraph(State)

builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode([set_budget, get_balance, generate_menu, recalculate, create_order]))

builder.set_entry_point("agent")
builder.add_conditional_edges(
    source="agent",
    path=should_continue,
)
builder.add_edge("tools", "agent")

graph = builder.compile()


__all__ = ["graph"]
