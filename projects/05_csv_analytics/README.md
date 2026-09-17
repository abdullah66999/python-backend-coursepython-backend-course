# 05 CSV Analytics

Отчёт по продажам из CSV: чтение, Decimal, группировка и тесты.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python main.py data/sales.csv
python -m pytest
```

`analytics.py` содержит чистые функции и не печатает результат. `main.py` отвечает только за CLI.
