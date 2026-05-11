# LeBlog — Blog personnel Django

Un blog personnel construit from scratch avec Django, conçu pour documenter mon apprentissage du développement web.

## Aperçu

Ce projet est à la fois un blog fonctionnel et un portfolio technique. J'y publie ce que j'apprends — Django, Python, HTML/CSS — avec des articles, des catégories, et une section commentaires.

## Fonctionnalités

- Liste des articles avec article mis en avant
- Détail d'un article avec commentaires
- Système de catégories cliquables
- Formulaire de contact sauvegardé en base
- Page À propos
- Authentification (login / logout)
- Interface d'administration Django
- Design éditorial responsive (CSS custom, Google Fonts)

## Stack technique

- **Backend** — Python 3.14, Django 6
- **Base de données** — SQLite (développement)
- **Frontend** — HTML, CSS custom (sans framework)
- **Fonts** — Playfair Display, DM Sans

## Installation locale

### Prérequis
- Python 3.10+
- pip

### Étapes

```bash
# 1. Cloner le repo
git clone https://github.com/TheN8Learner/django-blog.git
cd django-blog

# 2. Créer et activer l'environnement virtuel
python -m venv env
source env/bin/activate        # Mac/Linux
env\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Remplir .env avec ta propre SECRET_KEY

# 5. Appliquer les migrations
python manage.py migrate

# 6. Créer un superutilisateur
python manage.py createsuperuser

# 7. Lancer le serveur
python manage.py runserver
```

L'application est accessible sur `http://127.0.0.1:8000`
L'admin Django sur `http://127.0.0.1:8000/admin`

## Variables d'environnement

Créer un fichier `.env` à la racine du projet :

```
SECRET_KEY=your_secret_key_here
DEBUG=True
```

## Structure du projet

```
myBlog/
├── Blog/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── blog.html
│   │   ├── article_details.html
│   │   ├── categories.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── registration/
│   │       └── login.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── myBlog/
│   └── settings.py
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Modèles

| Modèle | Champs principaux |
|--------|------------------|
| `Post` | title, content, author, category, is_published, created_at |
| `Category` | name |
| `Commentaire` | texte, auteur, post, created_at |
| `Contact` | nom, prenom, email, message, created_at |

## À venir

- [ ] Pagination
- [ ] CRUD articles depuis le site
- [ ] Recherche par mot-clé
- [ ] Déploiement

## Auteur

**TheN8Learner** — apprenti développeur, j'apprends en construisant.  
GitHub : [@TheN8Learner](https://github.com/TheN8Learner)
