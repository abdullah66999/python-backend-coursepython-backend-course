import argparse
import json
from pathlib import Path

from search import find_matches


def main() -> None:
    parser = argparse.ArgumentParser(description="Поиск в документах")
    parser.add_argument("root", type=Path)
    parser.add_argument("query")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = find_matches(args.root, args.query)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for item in result:
            print(f"{item['path']}:{item['line']}: {item['text']}")


if __name__ == "__main__":
    main()
