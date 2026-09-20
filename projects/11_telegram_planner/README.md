# 11 Telegram Planner Bot

Учебный Telegram-бот на aiogram 3: `/start`, `/add`, `/tasks`, FSM, inline-кнопка завершения и SQLite.

## Запуск локально

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cp .env.example .env           # Windows: copy .env.example .env
# впишите токен от @BotFather в .env
set -a && source .env && set +a
python -m app
```

PowerShell:

```powershell
$env:BOT_TOKEN="токен"
python -m app
```

## Проверки

```bash
python -m pytest
```

Токен не хранится в исходниках и не нужен для запуска тестов. Для production добавьте Redis FSM storage, PostgreSQL, webhook через HTTPS, логи и CI.
