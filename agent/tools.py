import sys
from pathlib import Path
from langchain_core.tools import tool

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def make_tools(user_id: int) -> list:

    @tool
    def set_budget(amount: int) -> str:
        """
        Установить недельный бюджет пользователя.
        Вызывай когда пользователь говорит:
        'установи бюджет X', 'бюджет на неделю X', 'хочу тратить X в неделю'.
        Остаток (balance) также сбрасывается до нового значения.
        """
        from database import update_budget
        update_budget(user_id, amount)
        return f"Бюджет {amount} руб. установлен. Остаток также обновлён до {amount} руб."

    @tool
    def get_balance() -> str:
        """
        Получить текущий бюджет и остаток пользователя.
        Вызывай когда пользователь говорит:
        'сколько осталось', 'какой бюджет', 'покажи баланс', 'сколько денег'.
        """
        from database import get_user
        user = get_user(user_id)
        if user is None:
            return "Пользователь не найден"
        return f"Бюджет: {user['budget']} руб., Остаток: {user['balance']} руб."

    @tool
    def recalculate(amount: int, description: str) -> str:
        """
        Записать расход или доход и пересчитать остаток бюджета.
        Вызывай когда пользователь говорит:
        'потратил X', 'купил за X', 'заплатил X' — передавай amount отрицательным (-X).
        'получил X', 'заработал X', 'пришло X' — передавай amount положительным (+X).
        description — краткое описание операции (например: 'продукты', 'зарплата').
        """
        from database import update_balance, get_user
        update_balance(user_id, amount)
        user = get_user(user_id)
        return f"Записано: {description} ({amount:+} руб.). Новый остаток: {user['balance']} руб."

    @tool
    def generate_menu(day: str = None) -> str:
        """
        Сгенерировать меню на конкретный день (завтрак, обед, ужин) с учётом бюджета.
        Вызывай когда пользователь говорит:
        'составь меню', 'что поесть на [день]', 'план питания на [день]'.
        После вызова — предложи конкретные блюда с примерными ценами, уложись в остаток бюджета и больше ничего не пиши.
        Если день не указан — используй сегодняшний.
        """
        from database import get_user
        user = get_user(user_id)
        balance = user['balance'] if user else 0
        return (
            f"Остаток бюджета: {balance} руб. "
        )

    @tool
    def generate_dish(day: str = None, meal_type: str = None) -> str:
        """
        Сгенерировать одно блюдо на конкретный приём пищи с учётом бюджета.
        Вызывай когда пользователь говорит:
        'что приготовить на завтрак/обед/ужин', 'предложи блюдо на [приём пищи]'.
        meal_type — один из: завтрак, обед, ужин.
        После вызова — предложи конкретное блюдо с примерной ценой, уложись в остаток бюджета и больше ничего не пиши.
        Если день не указан — используй сегодняшний.
        """
        from database import get_user
        user = get_user(user_id)
        balance = user['balance'] if user else 0
        return (
            f"Остаток бюджета: {balance} руб. "
        )

    @tool
    def create_order(items: list[str]) -> str:
        """
        Сформировать список продуктов для покупки (корзину).
        Вызывай когда пользователь говорит:
        'составь список покупок', 'что купить', 'добавь в корзину X'.
        items — список продуктов, которые нужно купить.
        """
        return f"Корзина: {items}"

    return [set_budget, get_balance, recalculate, generate_menu, generate_dish, create_order]