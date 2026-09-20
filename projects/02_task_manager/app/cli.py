import argparse
from pathlib import Path

from . import repository, service


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Менеджер задач")
    sub = result.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add")
    add.add_argument("title")
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--open", action="store_true")
    done = sub.add_parser("done")
    done.add_argument("id", type=int)
    stats = sub.add_parser("stats")
    return result


def main() -> None:
    args = parser().parse_args()
    db_path = Path("tasks.db")
    with repository.connect(db_path) as connection:
        try:
            if args.command == "add":
                task_id = service.add_task(connection, args.title)
                print(f"Добавлена задача #{task_id}")
            elif args.command == "list":
                for task in repository.list_tasks(connection, args.open):
                    mark = "x" if task["done"] else " "
                    print(f"{task['id']:>3} [{mark}] {task['title']}")
            elif args.command == "done":
                if not repository.complete(connection, args.id):
                    raise ValueError("Задача не найдена")
                print("Задача выполнена")
            elif args.command == "stats":
                tasks = repository.list_tasks(connection)
                done = sum(task["done"] for task in tasks)
                print(f"Всего: {len(tasks)}, выполнено: {done}")
        except ValueError as error:
            print(f"Ошибка: {error}")
            raise SystemExit(2) from error
