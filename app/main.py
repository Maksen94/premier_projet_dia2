from fastapi import FastAPI, HTTPException

from app.math import factorielle

app = FastAPI(title="Mini API")


@app.get("/math/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))