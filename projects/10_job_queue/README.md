# 10 Async Job Queue

Локальная очередь фоновых задач на `asyncio`: producer, worker, попытки и graceful shutdown.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python queue_service.py
python -m pytest
```

Это учебная очередь внутри одного процесса. Для нескольких экземпляров сервиса замените её Redis/RQ/Celery.
