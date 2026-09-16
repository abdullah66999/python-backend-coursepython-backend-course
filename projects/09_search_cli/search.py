import re
from pathlib import Path


def find_matches(root: Path, query: str) -> list[dict]:
    try:
        pattern = re.compile(query, re.IGNORECASE)
    except re.error as error:
        raise ValueError(f"Неверный шаблон: {error}") from error
    matches = []
    for path in root.rglob("*.md"):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                matches.append({"path": str(path), "line": number, "text": line.strip()})
    return matches
