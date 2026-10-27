# Mini API Python

![CI](https://github.com/Maksen94/premier_projet_dia2/actions/workflows/ci.yml/badge.svg)

API de petits outils (maths, texte, conversion, validation) développée en équipe avec FastAPI.

## Installation

Prérequis : Python 3.12 ou plus récent.

```bash
git clone https://github.com/Maksen94/premier_projet_dia2.git
cd premier_projet_dia2
python -m pip install -r requirements.txt
```

## Lancement

### En local

```bash
python -m uvicorn app.main:app --reload
```

L'API est disponible sur http://localhost:8000 et sa documentation interactive sur http://localhost:8000/docs.

### Avec Docker

[À compléter quand le Dockerfile sera fusionné]

```bash
docker build -t mini-api .
docker run -p 8000:8000 mini-api
```

## Utilisation

Exemples de requêtes :

| Route | Exemple | Réponse |
|---|---|---|
| `GET /email-valide` | `/email-valide?email=lea@mail.fr` | `{"email": "lea@mail.fr", "valide": true}` |
| `GET /mdp-robuste` | `/mdp-robuste?mdp=Abcdef1!` | `{"valide": true}` |
| `GET /code-postal` | `/code-postal?cp=94000` | `{"code_postal": "94000", "valide": true}` |

Une entrée invalide (par exemple vide) renvoie une erreur **400** avec un message explicatif.
Les routes des modules math, texte et conversion sont listées sur `/docs`.

## Tests

```bash
python -m pytest
python -m pytest --cov=app --cov-fail-under=80
python -m ruff check .
```

La CI GitHub Actions lance ruff et pytest (couverture minimale de 80 %) à chaque push et pull request.

## Contribuer

1. Créer une issue décrivant la tâche.
2. Créer une branche depuis `main` à jour : `type/numéro-description` (ex. `feat/12-code-postal`).
3. Faire des commits atomiques au format Conventional Commits : `feat(validation): ajoute code_postal`.
4. Ouvrir une pull request vers `main` avec `Closes #numéro`.
5. Attendre la CI verte et l'approbation d'un autre membre, puis fusionner.

Personne ne pousse directement sur `main`.

## Structure du projet

```
app/            code de l'API (main.py, erreurs.py, math.py, outils/)
tests/          tests automatisés
.github/        workflows CI/CD
requirements.txt
ruff.toml
```

## Équipe

| Membre | Module |
|---|---|
| maltaarianne6-sudo | validation |
| Maksen94 | texte |
| Selyanmtl | conversion |
| siham2006-HUB | math |

## Licence

[À compléter quand le fichier LICENSE sera ajouté, par exemple MIT]