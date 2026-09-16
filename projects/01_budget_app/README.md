# 01 Budget App

Консольный калькулятор бюджета. В проекте показано разделение расчётов и пользовательского ввода.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python main.py
python -m pytest
```

## Что изучить

- `budget.py` — чистые функции и Decimal;
- `main.py` — цикл ввода и обработка ошибок;
- `tests/test_budget.py` — тесты обычных и граничных случаев.
