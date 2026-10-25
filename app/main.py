from fastapi import FastAPI, HTTPException

from app.outils.validation import email_valide
from app.math import est_premier, factorielle, pgcd

app = FastAPI(title="Mini API")


@app.get("/email-valide")
def route_email_valide(email: str):
    try:
        return {"email": email, "valide": email_valide(email)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
@app.get("/math/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/math/est_premier/{n}")
def route_est_premier(n: int):
    try:
        return {"n": n, "resultat": est_premier(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/math/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int):
    try:
        return {"a": a, "b": b, "resultat": pgcd(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
