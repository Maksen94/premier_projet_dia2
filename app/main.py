from fastapi import FastAPI, HTTPException

from app.math import factorielle
from app.math import est_premier, factorielle

app = FastAPI(title="Mini API")


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