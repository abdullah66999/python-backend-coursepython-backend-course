# 07 Webhook Receiver

Приём webhook с HMAC-подписью и защитой от повторной доставки.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app:app --reload
python -m pytest
```

Для учебного запуска секрет фиксирован в переменной `WEBHOOK_SECRET`. В production используйте secrets manager.
