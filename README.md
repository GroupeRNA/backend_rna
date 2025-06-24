# Projet backend RNA 
Projet RNA backend en django


## 🔧 Technologies utilisées

- [Python 3.10.12](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

## 🚀 Installation locale

Voici les étapes pour lancer le projet en local :

### 1. Cloner le dépôt

```bash
git clone https://github.com/razafindrakoto1234/GroupeRNA/backend_rna.git
cd backend_rna


### 2. Création du variable d'environnement
python -m venv env

### 3. Activer l'environnement virtuel
## sous Linux/MacOS
source env/bin/activate

## sous Windows
env\Scripts\activate

### 4. Installation des dépendances
pip install -r requirements.txt

### 5. COnfiguration de la base de donnée
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

### 6. Appliquer les migrations
python manage.py migrate

### 7. Lancer le serveur de développement 
python manage.py runserver