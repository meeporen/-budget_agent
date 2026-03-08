import sys
import re
from pathlib import Path
from datetime import datetime

from langchain_core.messages import HumanMessage, SystemMessage

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from agent.graph import make_graph
from database import get_user, create_user


def answer_agent(user_id: int, user_message: str) -> str:
    if get_user(user_id) is None:
        create_user(user_id)

    DAYS = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    today = DAYS[datetime.now().weekday()]

    state = {
        "user_id": user_id,
        "budget": None,
        "balance": None,
        "day_of_week": datetime.now().weekday(),
        "messages": [
            SystemMessage(content=(
                "Ты помощник по управлению личным бюджетом. "
                "Отвечай на русском языке. "
                "Никогда не упоминай названия инструментов пользователю. "
                "Сам определяй какое действие нужно выполнить по контексту сообщения. "
                f"Сегодня {today}. Если пользователь не уточняет день — используй сегодняшний. "
                "Отвечай коротко и по делу."
            )),
            HumanMessage(content=user_message),
        ],
        "tool_call": None,
        "response": None,
    }

    answer = make_graph(user_id).invoke(state)

    text = answer["messages"][-1].content
    clean_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL, count=1).strip()
    return clean_text
