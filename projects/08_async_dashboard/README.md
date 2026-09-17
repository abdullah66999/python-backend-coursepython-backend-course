# 08 Async Dashboard

Асинхронный агрегатор профиля, баланса и уведомлений. Внешние запросы имитируются `MockTransport`, поэтому тесты не зависят от интернета.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python dashboard.py
python -m pytest
```
