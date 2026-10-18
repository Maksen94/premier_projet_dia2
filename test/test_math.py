import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.math import factorielle

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