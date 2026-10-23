from fastapi import FastAPI, HTTPException

from app.outils.validation import email_valide

app = FastAPI(title="Mini API")


@app.get("/email-valide")
def route_email_valide(email: str):
    try:
        return {"email": email, "valide": email_valide(email)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))