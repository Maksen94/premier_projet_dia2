# app/texte.py

def inverser(chaine: str) -> str:
    # Cas d'erreur : on refuse si l'utilisateur n'entre que des chiffres
    if chaine.isdigit():
        raise ValueError("L'entrée doit contenir des lettres, pas seulement des nombres.")
    
    # En Python, [::-1] est une astuce qui lit une chaîne à l'envers
    return chaine[::-1]