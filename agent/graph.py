from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from agent.state import State
from agent.llm import llm
from agent.tools import make_tools


def make_graph(user_id: int):
    tools = make_tools(user_id)
    llm_with_tools = llm.bind_tools(tools)

    def agent_node(state: State) -> dict:
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    def should_continue(state: State) -> str:
        if state["messages"][-1].tool_calls:
            return "tools"
        return END

    builder = StateGraph(State)
    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(tools))
    builder.set_entry_point("agent")
    builder.add_conditional_edges(source="agent", path=should_continue)
    builder.add_edge("tools", "agent")

    return builder.compile()
