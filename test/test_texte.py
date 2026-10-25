# tests/test_texte.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# --- TESTS POUR INVERSER ---
def test_inverser_normal():
    reponse = client.get("/texte/inverser/bonjour")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == "ruojnob"

def test_inverser_limite():
    reponse = client.get("/texte/inverser/a")
    assert reponse.status_code == 200
    assert reponse.json()["resultat"] == "a"


# --- TESTS POUR PALINDROME ---
def test_palindrome_normal():
    reponse = client.get("/texte/palindrome/kayak")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True

def test_palindrome_limite():
    reponse = client.get("/texte/palindrome/ressasser")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True


# --- TESTS POUR VOYELLES ---
def test_voyelles_normal():
    reponse = client.get("/texte/voyelles/bonjour")
    assert reponse.status_code == 200
    assert reponse.json()["nombre_voyelles"] == 3

def test_voyelles_limite():
    # 'y' est compté comme une voyelle, donc 1 voyelle dans 'xyz'
    reponse = client.get("/texte/voyelles/xyz")
    assert reponse.status_code == 200
    assert reponse.json()["nombre_voyelles"] == 1