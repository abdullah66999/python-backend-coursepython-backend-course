# 03 Notes API

Полностью запускаемый учебный API на FastAPI и SQLAlchemy. Для простоты по умолчанию используется SQLite, поэтому проект запускается без внешней базы.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
python -m pytest
```

Откройте `http://127.0.0.1:8000/docs`. Входные данные проходят Pydantic-валидацию, пустой title отклоняется с 422, неизвестная заметка возвращает 404.
