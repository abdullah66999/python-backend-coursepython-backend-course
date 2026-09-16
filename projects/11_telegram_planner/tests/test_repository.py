import sqlite3

import pytest

from app import repository


@pytest.fixture
def connection():
    connection = repository.connect(":memory:")
    yield connection
    connection.close()


def test_user_sees_only_own_tasks(connection):
    repository.add_task(connection, 7, "Первая")
    repository.add_task(connection, 8, "Чужая")
    own = repository.list_open(connection, 7)
    assert [task["title"] for task in own] == ["Первая"]


def test_complete_is_scoped_to_user(connection):
    task_id = repository.add_task(connection, 7, "Первая")
    assert repository.complete_task(connection, 8, task_id) is False
    assert repository.complete_task(connection, 7, task_id) is True
