import sys
from pathlib import Path

from analytics import load_sales, totals_by_product


def main() -> None:
    sales = load_sales(Path(sys.argv[1]))
    for product, total in sorted(totals_by_product(sales).items()):
        print(f"{product}: {total:.2f}")


if __name__ == "__main__":
    main()
