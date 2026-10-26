# app/main.py
from fastapi import FastAPI, HTTPException

from app.outils.validation import email_valide, mdp_robuste



# 1. Initialisation de l'application en premier
app = FastAPI(title="Mini API")

# 2. Tous les imports de vos modules
from app.outils.texte import inverser, est_palindrome, compter_voyelles
from app.outils.conversion import celsius_fahrenheit, km_miles, euros_devise



from app.math import est_premier, factorielle, pgcd


# --- ROUTES TEXTE ---
@app.get("/texte/inverser/{chaine}")
def route_inverser(chaine: str):
    try:
        return {"chaine": chaine, "resultat": inverser(chaine)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/texte/palindrome/{texte}")
def route_palindrome(texte: str):
    try:
        return {"texte": texte, "est_palindrome": est_palindrome(texte)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/texte/voyelles/{texte}")
def route_voyelles(texte: str):
    try:
        return {"texte": texte, "nombre_voyelles": compter_voyelles(texte)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# --- ROUTES VALIDATION ---
@app.get("/email-valide")
def route_email_valide(email: str):
    try:
        return {"email": email, "valide": email_valide(email)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


# --- ROUTES MATHS ---




@app.get("/mdp-robuste")
def route_mdp_robuste(mdp: str):
    try:
        return {"valide": mdp_robuste(mdp)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
    


@app.get("/math/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/math/est_premier/{n}")
def route_est_premier(n: int):
    try:
        return {"n": n, "resultat": est_premier(n)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/math/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int):
    try:
        return {"a": a, "b": b, "resultat": pgcd(a, b)}
    except ValueError as e:

        raise HTTPException(400, detail=str(e))

        raise HTTPException(status_code=400, detail=str(e))

# --- ROUTES CONVERSION ---
@app.get("/conversion/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    try:
        return {"celsius": celsius, "fahrenheit": celsius_fahrenheit(celsius)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/conversion/km_miles/{km}")
def route_km_miles(km: float):
    try:
        return {"km": km, "miles": km_miles(km)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/conversion/euros_devise/{montant}/{devise}")
def route_euros_devise(montant: float, devise: str):
    try:
        return {"montant": montant, "devise": devise.upper(), "resultat": euros_devise(montant, devise)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))

