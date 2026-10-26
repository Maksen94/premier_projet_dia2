import pytest
from app.outils.conversion import celsius_fahrenheit, km_miles, euros_devise


# --- celsius_fahrenheit ---
def test_celsius_fahrenheit_ebullition():
    assert celsius_fahrenheit(100) == pytest.approx(212)


def test_celsius_fahrenheit_zero_absolu():
    assert celsius_fahrenheit(-273.15) == pytest.approx(-459.67)


def test_celsius_fahrenheit_sous_zero_absolu():
    with pytest.raises(ValueError):
        celsius_fahrenheit(-300)


# --- km_miles ---
def test_km_miles_normal():
    assert km_miles(10) == pytest.approx(6.21371)


def test_km_miles_zero():
    assert km_miles(0) == 0


def test_km_miles_negatif():
    with pytest.raises(ValueError):
        km_miles(-1)


# --- euros_devise ---
def test_euros_devise_normal():
    assert euros_devise(100, "USD") == pytest.approx(108)


def test_euros_devise_minuscules():
    assert euros_devise(100, "usd") == pytest.approx(108)


def test_euros_devise_montant_negatif():
    with pytest.raises(ValueError):
        euros_devise(-5, "USD")


def test_euros_devise_devise_inconnue():
    with pytest.raises(ValueError):
        euros_devise(100, "XXX")