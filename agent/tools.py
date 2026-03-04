from langchain_core.tools import tool


@tool
def set_budget(amount: int) -> str:
    """Установить бюджет на неделю"""
    return f"Бюджет {amount}₽ установлен"


@tool
def get_balance() -> str:
    """Получить текущий остаток бюджета"""
    return "Остаток: 0₽"


@tool
def generate_menu(day: str = None, meal_type: str = None) -> str:
    """
    Используй эту функцию, если пользователь просит предложить блюдо
    или сгенерировать меню на конкретный день недели
    или на конкретный прием пищи (завтрак, обед, ужин).
    """
    return f"{meal_type} в {day}"


@tool
def recalculate(amount: int, description: str) -> str:
    """Перерасчитать бюджет (расход/доход)"""
    return f"Перерасчёт: {amount}₽ ({description})"


@tool
def create_order(items: list[str]) -> str:
    """Сформировать корзину продуктов"""
    return f"Корзина: {items}"


__all__ = ["set_budget", "get_balance", "generate_menu", "recalculate", "create_order"]
