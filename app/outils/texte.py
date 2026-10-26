# app/outils/texte.py

def est_palindrome(texte: str) -> bool:
    if not isinstance(texte, str):
        raise ValueError("L'entrée doit être une chaîne de caractères")
    nettoye = "".join(texte.lower().split())
    return nettoye == nettoye[::-1]

def compter_voyelles(texte: str) -> int:
    if not isinstance(texte, str):
        raise ValueError("L'entrée doit être une chaîne de caractères")
    voyelles = "aeiouyàâäéèêëîïôöùûüÿ"
    return sum(1 for c in texte.lower() if c in voyelles)

def inverser(texte: str) -> str:
    if not isinstance(texte, str):
        raise ValueError("L'entrée doit être une chaîne de caractères")
    return texte[::-1]