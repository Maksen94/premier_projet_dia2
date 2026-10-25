import re
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[\w-]+$")
def email_valide(email : str) -> bool:
    if not isinstance(email, str) or not email.strip():
        raise ValueError("l'email ne doit pas être vide")
    return bool(EMAIL_RE.match(email))




def mdp_robuste(mdp: str) -> bool:
    if not isinstance(mdp, str) or not mdp:
        raise ValueError("le mot de passe ne doit pas être vide")
    if len(mdp) < 8:
        return False
    a_majuscule = any(c.isupper() for c in mdp)
    a_minuscule = any(c.islower() for c in mdp)
    a_chiffre = any(c.isdigit() for c in mdp)
    a_special = any(not c.isalnum() for c in mdp)
    return a_majuscule and a_minuscule and a_chiffre and a_special




def code_postal(cp: str) -> bool:
    if not isinstance(cp, str) or not cp.strip():
        raise ValueError("le code postal ne doit pas être vide")
    return bool(re.fullmatch(r"\d{5}", cp))