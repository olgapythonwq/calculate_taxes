import pytest

from src.taxes import calculate_taxes, calculate_tax


@pytest.fixture
def prices():
    return [100.0, 200.0, 300.0]


@pytest.mark.parametrize("tax_rate, expected", [
    (10.0, [110.0, 220.0, 330.0]),
    (15.0, [115.0, 230.0, 345.0]),
    (20.0, [120.0, 240.0, 360.0])
])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1], tax_rate=10.0)


@pytest.mark.parametrize("price, tax_rate, expected", [
    (100.0, 10.0, 110.0),
    (50.0, 5.0, 52.5)
])
def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


def test_calculate_tax_invalid_prices():
    with pytest.raises(ValueError):
        calculate_tax(-1, 10.0)


def test_calculate_tax_negative_tax_rate():
    with pytest.raises(ValueError):
        calculate_tax(100.0, -1)


def test_calculate_tax_tax_rate_above_100():
    with pytest.raises(ValueError):
        calculate_tax(100.0, 1000.0)
