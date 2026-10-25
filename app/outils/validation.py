import re
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[\w-]+$")
def email_valide(email : str) -> bool:
    if not isinstance(email, str) or not email.strip():
        raise ValueError("l'email ne doit pas être vide")
    return bool(EMAIL_RE.match(email))
