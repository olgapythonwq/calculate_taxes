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


@pytest.mark.parametrize("price, tax_rate, discount, expected", [
    (100.0, 10.0, 0.0, 110.0),
    (100.0, 10.0, 10.0, 99.0),
    (100.0, 10.0, 100.0, 0.0)
])
def test_calculate_tax_with_discount(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount=discount) == expected


def test_calculate_tax_with_no_discount():
    assert calculate_tax(100.0, 10.0) == 110.0


@pytest.mark.parametrize("round_digits, expected", [
    (0, 99.0),
    (1, 99.4),
    (2, 99.42),
    (3, 99.425),
])
def test_calculate_tax_round(round_digits, expected):
    assert calculate_tax(100.0, 2.5, discount=3, round_digits=round_digits) == expected


@pytest.mark.parametrize("price, tax_rate, discount, round_digits", [
    ('100.0', 10.0, 0.0, 1),
    (100.0, '10.0', 10.0, 1),
    (100.0, 10.0, '100.0', 1),
    (100.0, 10.0, 100.0, '1')
])
def test_calculate_tax_wrong_type(price, tax_rate, discount, round_digits):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, round_digits=round_digits)


def test_calculate_rax_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100, 2, 3, 10)
