from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")


def parse_amount(raw: str) -> Decimal:
    """Convert user text to a non-negative amount with two decimals."""
    try:
        value = Decimal(raw.strip().replace(",", "."))
    except InvalidOperation as error:
        raise ValueError("Введите число") from error
    if value < 0:
        raise ValueError("Сумма не может быть отрицательной")
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def calculate_balance(income: Decimal, expenses: list[Decimal]) -> tuple[Decimal, Decimal, Decimal]:
    total = sum(expenses, Decimal("0")).quantize(CENT)
    balance = (income - total).quantize(CENT)
    percent = Decimal("0") if income == 0 else (total / income * 100).quantize(CENT)
    return total, balance, percent
