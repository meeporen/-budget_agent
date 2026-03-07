import sys
from pathlib import Path
from langchain_core.tools import tool

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def make_tools(user_id: int) -> list:
    @tool
    def set_budget(amount: int) -> str:
        """Установить бюджет на неделю. Вызывай когда пользователь хочет установить недельный бюджет."""
        from database import update_budget
        update_budget(user_id, amount)
        return f"Бюджет {amount} руб. установлен. Остаток также обновлён до {amount} руб."

    @tool
    def get_balance() -> str:
        """Получить текущий бюджет и остаток пользователя"""
        from database import get_user
        user = get_user(user_id)
        if user is None:
            return "Пользователь не найден"
        return f"Бюджет: {user['budget']} руб., Остаток: {user['balance']} руб."

    @tool
    def generate_menu(day: str = None, meal_type: str = None) -> str:
        """
        Используй эту функцию, если пользователь просит предложить блюдо
        или сгенерировать меню на конкретный день недели
        или на конкретный прием пищи (завтрак, обед, ужин).
        """
        from database import get_user
        user = get_user(user_id)
        balance = user['balance'] if user else 0
        return (
            f"Остаток бюджета: {balance} руб. "
            f"Предложи блюдо на {meal_type} в {day} с учётом бюджета."
        )


    @tool
    def recalculate(amount: int, description: str) -> str:
        """Перерасчитать бюджет (расход/доход). amount может быть отрицательным для расхода."""
        from database import update_balance, get_user
        update_balance(user_id, amount)
        user = get_user(user_id)
        return f"Записано: {description} ({amount:+} руб.). Новый остаток: {user['balance']} руб."

    @tool
    def create_order(items: list[str]) -> str:
        """Сформировать корзину продуктов"""
        return f"Корзина: {items}"

    return [set_budget, get_balance, generate_menu, recalculate, create_order]
