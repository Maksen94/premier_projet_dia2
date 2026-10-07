# tests/test_texte.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# 1. Cas normal : On vérifie qu'un mot classique est bien inversé
def test_inverser_normal():
    reponse = client.get("/texte/inverser/bonjour")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == "ruojnob"

# 2. Cas limite : On vérifie le comportement avec une seule lettre
def test_inverser_limite():
    reponse = client.get("/texte/inverser/a")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == "a"

# 3. Cas d'erreur : On vérifie que les nombres déclenchent bien l'erreur 400
def test_inverser_erreur():
    reponse = client.get("/texte/inverser/12345")
    assert reponse.status_code == 400
    assert "L'entrée doit contenir des lettres" in reponse.json()["detail"]