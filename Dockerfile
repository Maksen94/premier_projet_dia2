FROM python:3.12-slim

WORKDIR /app

# Empêche Python d'écrire des fichiers .pyc et assure la diffusion immédiate des logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code applicatif
COPY app/ ./app

# Utilisateur non-root pour la sécurité
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

