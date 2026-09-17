from decimal import Decimal

from analytics import Sale, totals_by_product


def test_totals_by_product():
    sales = [Sale("Чай", Decimal("10.00")), Sale("Чай", Decimal("2.50"))]
    assert totals_by_product(sales)["Чай"] == Decimal("12.50")
