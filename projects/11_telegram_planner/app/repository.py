import sqlite3
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
)
"""


def connect(path: str | Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute(SCHEMA)
    connection.commit()
    return connection


def add_task(connection: sqlite3.Connection, telegram_id: int, title: str) -> int:
    cursor = connection.execute(
        "INSERT INTO tasks (telegram_id, title) VALUES (?, ?)",
        (telegram_id, title),
    )
    connection.commit()
    return int(cursor.lastrowid)


def list_open(connection: sqlite3.Connection, telegram_id: int) -> list[sqlite3.Row]:
    return connection.execute(
        "SELECT id, title FROM tasks WHERE telegram_id = ? AND done = 0 ORDER BY id",
        (telegram_id,),
    ).fetchall()


def complete_task(connection: sqlite3.Connection, telegram_id: int, task_id: int) -> bool:
    cursor = connection.execute(
        "UPDATE tasks SET done = 1 WHERE id = ? AND telegram_id = ?",
        (task_id, telegram_id),
    )
    connection.commit()
    return cursor.rowcount == 1
