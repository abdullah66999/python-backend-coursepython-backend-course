# 09 Search CLI

Поиск по Markdown-файлам с номером строки, JSON-режимом и обработкой плохого регулярного выражения.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python cli.py docs Python
python cli.py docs Python --json
python -m pytest
```
