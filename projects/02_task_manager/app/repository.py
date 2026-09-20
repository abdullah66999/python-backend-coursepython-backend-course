import sqlite3
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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


def add(connection: sqlite3.Connection, title: str) -> int:
    cursor = connection.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    connection.commit()
    return int(cursor.lastrowid)


def list_tasks(connection: sqlite3.Connection, open_only: bool = False) -> list[sqlite3.Row]:
    if open_only:
        return connection.execute("SELECT * FROM tasks WHERE done = 0 ORDER BY id").fetchall()
    return connection.execute("SELECT * FROM tasks ORDER BY id").fetchall()


def complete(connection: sqlite3.Connection, task_id: int) -> bool:
    cursor = connection.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    connection.commit()
    return cursor.rowcount == 1


def delete(connection: sqlite3.Connection, task_id: int) -> bool:
    cursor = connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    return cursor.rowcount == 1
