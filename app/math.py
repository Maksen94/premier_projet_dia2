def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    if n > 1000:
        raise ValueError("n doit être inférieur ou égal à 1000")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


def est_premier(n: int) -> bool:
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def pgcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("a et b doivent être positifs ou nuls")
    if a == 0 and b == 0:
        raise ValueError("pgcd(0, 0) n'est pas défini")
    while b:
        a, b = b, a % b
    return a

