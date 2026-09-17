# 02 Task Manager

Менеджер задач в терминале. База SQLite создаётся автоматически, данные сохраняются после перезапуска.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m app add "Изучить SQLite"
python -m app list
python -m app done 1
python -m app stats
python -m pytest
```

Слой `repository.py` отвечает за SQLite, `service.py` — за правила, `cli.py` — за терминал. Тесты используют временную базу.
