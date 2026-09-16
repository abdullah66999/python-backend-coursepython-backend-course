import csv
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class Sale:
    product: str
    amount: Decimal


def load_sales(path: Path) -> list[Sale]:
    with path.open(newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        return [Sale(row["product"], Decimal(row["amount"])) for row in rows]


def totals_by_product(sales: list[Sale]) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for sale in sales:
        totals[sale.product] = totals.get(sale.product, Decimal("0")) + sale.amount
    return totals
