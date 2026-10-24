import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.math import est_premier, factorielle, pgcd

client = TestClient(app)


def test_factorielle_normal():
    assert factorielle(5) == 120


def test_factorielle_limite():
    assert factorielle(0) == 1


def test_factorielle_erreur():
    with pytest.raises(ValueError):
        factorielle(-1)


def test_route_factorielle():
    r = client.get("/math/factorielle/5")
    assert r.status_code == 200
    assert r.json()["resultat"] == 120
    assert client.get("/math/factorielle/-1").status_code == 400


def test_est_premier_normal():
    assert est_premier(17) is True
    assert est_premier(18) is False


def test_est_premier_limite():
    assert est_premier(0) is False
    assert est_premier(1) is False
    assert est_premier(2) is True


def test_est_premier_erreur():
    with pytest.raises(ValueError):
        est_premier(-7)


def test_route_est_premier():
    r = client.get("/math/est_premier/13")
    assert r.status_code == 200
    assert r.json()["resultat"] is True
    assert client.get("/math/est_premier/-3").status_code == 400


def test_pgcd_normal():
    assert pgcd(48, 18) == 6


def test_pgcd_limite():
    assert pgcd(0, 5) == 5


def test_pgcd_erreur():
    with pytest.raises(ValueError):
        pgcd(-4, 6)
    with pytest.raises(ValueError):
        pgcd(0, 0)


def test_route_pgcd():
    r = client.get("/math/pgcd/48/18")
    assert r.status_code == 200
    assert r.json()["resultat"] == 6
    assert client.get("/math/pgcd/0/0").status_code == 400