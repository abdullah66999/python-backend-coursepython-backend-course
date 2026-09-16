from . import repository


def normalize_title(title: str) -> str:
    title = title.strip()
    if not title:
        raise ValueError("Название задачи не может быть пустым")
    return title


def add_task(connection, title: str) -> int:
    return repository.add(connection, normalize_title(title))
