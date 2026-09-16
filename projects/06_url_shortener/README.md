# 06 URL Shortener

Мини-сервис коротких ссылок на FastAPI. Хранилище в памяти оставлено намеренно: сначала изучите HTTP-контракт, затем замените его repository.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app:app --reload
python -m pytest
```
