# app/main.py
from fastapi import FastAPI, HTTPException
from app.texte import inverser

# Ton app = FastAPI() doit déjà être au début du fichier

@app.get("/texte/inverser/{chaine}")
def route_inverser(chaine: str):
    try:
        return {"chaine": chaine, "resultat": inverser(chaine)}
    except ValueError as e:
        # On intercepte l'erreur de notre fonction et on la transforme en erreur Web 400
        raise HTTPException(status_code=400, detail=str(e))