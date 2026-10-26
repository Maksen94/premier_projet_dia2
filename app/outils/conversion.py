# app/outils/conversion.py

TAUX_EUR = {
    "USD": 1.08,
    "GBP": 0.86,
    "JPY": 163.0,
}


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("la température ne peut pas être sous le zéro absolu")
    return celsius * 9 / 5 + 32


def km_miles(km: float) -> float:
    if km < 0:
        raise ValueError("la distance ne peut pas être négative")
    return km * 0.621371


def euros_devise(montant: float, devise: str) -> float:
    if montant < 0:
        raise ValueError("le montant ne peut pas être négatif")
    devise = devise.upper()
    if devise not in TAUX_EUR:
        raise ValueError(f"devise non supportée : {devise}")
    return montant * TAUX_EUR[devise]