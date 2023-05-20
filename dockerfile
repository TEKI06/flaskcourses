# Utilisez l'image de base Python 3.9
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers de l'application dans le conteneur
COPY . /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port sur lequel l'application Flask écoute
EXPOSE 5000

# Commande pour exécuter l'application Flask lors du démarrage du conteneur
CMD ["python", "app.py"]
