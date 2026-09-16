from decimal import Decimal

import pytest

from budget import calculate_balance, parse_amount


def test_parse_amount_accepts_comma():
    assert parse_amount("12,345") == Decimal("12.35")


def test_parse_amount_rejects_negative():
    with pytest.raises(ValueError):
        parse_amount("-1")


def test_calculate_balance():
    result = calculate_balance(Decimal("1000"), [Decimal("200"), Decimal("300")])
    assert result == (Decimal("500.00"), Decimal("500.00"), Decimal("50.00"))


def test_zero_income_does_not_divide_by_zero():
    assert calculate_balance(Decimal("0"), [Decimal("10")])[2] == Decimal("0")
