import sqlite3

import pytest

from app import repository, service


@pytest.fixture
def connection():
    connection = repository.connect(":memory:")
    yield connection
    connection.close()


def test_add_and_list(connection):
    task_id = service.add_task(connection, "Изучить SQLite")
    rows = repository.list_tasks(connection)
    assert task_id == 1
    assert rows[0]["title"] == "Изучить SQLite"


def test_empty_title_is_rejected(connection):
    with pytest.raises(ValueError):
        service.add_task(connection, " ")


def test_complete_unknown_task_returns_false(connection):
    assert repository.complete(connection, 999) is False
