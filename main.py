from agent.graph import graph
from langchain_core.messages import HumanMessage


# # Тест 1: Установка бюджета
# print("=" * 50)
# print("Тест 1: Установка бюджета")
# print("=" * 50)
#
# state = {
#     "user_id": 1,
#     "user_message": "Установи бюджет 5000",
#     "budget": None,
#     "balance": None,
#     "day_of_week": 0,
#     "messages": [HumanMessage(content="Установи бюджет 5000")],
#     "tool_call": None,
#     "response": None,
# }
#
# result = graph.invoke(state)
# print("Ответ:", result["messages"][-1].content)
#
#
# # Тест 2: Проверка баланса
# print("\n" + "=" * 50)
# print("Тест 2: Проверка баланса")
# print("=" * 50)
#
# state2 = {
#     "user_id": 1,
#     "user_message": "Сколько осталось денег?",
#     "budget": None,
#     "balance": None,
#     "day_of_week": 0,
#     "messages": [HumanMessage(content="Сколько осталось денег?")],
#     "tool_call": None,
#     "response": None,
# }
#
# result2 = graph.invoke(state2)
# print("Ответ:", result2["messages"][-1].content)


# Тест 3: Генерация меню
print("\n" + "=" * 50)
print("Тест 3: Генерация меню")
print("=" * 50)

state3 = {
    "user_id": 1,
    "budget": None,
    "balance": None,
    "day_of_week": 0,
    "messages": [HumanMessage(content="Предложи блюдо на ужин в пятницу")],
    "tool_call": None,
    "response": None,
}

result3 = graph.invoke(state3)
print("Ответ:", result3["messages"].content)
print(result3["messages"][-1])
