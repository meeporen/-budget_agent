import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "budget.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Создать таблицы, если их нет"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            budget INTEGER DEFAULT 0,
            balance INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def get_user(user_id: int) -> dict | None:
    """Получить данные пользователя"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, budget, balance FROM users WHERE user_id = ?",
        (user_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        return dict(row)
    return None


def create_user(user_id: int) -> dict:
    """Создать нового пользователя"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (user_id,)
    )
    
    conn.commit()
    conn.close()
    
    return {"user_id": user_id, "budget": 0, "balance": 0}


def update_budget(user_id: int, amount: int):
    """Установить бюджет пользователю"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET budget = ?, balance = ? WHERE user_id = ?",
        (amount, amount, user_id)
    )
    
    conn.commit()
    conn.close()


def update_balance(user_id: int, amount: int):
    """Изменить баланс (расход/доход)"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id = ?",
        (amount, user_id)
    )
    
    conn.commit()
    conn.close()

def get_balance(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT budget FROM users WHERE user_id = ?",

    )
    row = cursor.fetchone()
    conn.close()
    return row[0]


def delete_user(user_id: int):
    """Удалить пользователя"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

    conn.commit()
    conn.close()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    return rows



if __name__ == "__main__":
    init_db()
