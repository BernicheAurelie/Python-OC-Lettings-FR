## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Docker:

#### Dockerfile:

Le Dockerfile sera utilisé par docker pour créer notre image:

- installer et mettre a jour python3 et postgresql
- installer et mettre a jour pip
- installer les dépendances incluses dans requirements.txt
- spécifier les chemin de destination 
- gérer les fichier statiques
- spécifie le port exposé
- spécifier le serveur et le module wsgi utilisés

#### Build and push:

Création de l'image et lancement du conteneur en local:

- ``$ docker build --tag oc_lettings_site:latest .``
- ``$ docker run --name oc_lettings_site -dp 127.0.0.1:8000:8000 oc_lettings_site:latest``

Envoi sur DockerHub:
 - `$ docker login -u <username>`
 - `$ docker tag oc_lettings_site <username>/oc_lettings_site`
 - `$ docker push <username>/oc_lettings_site`


### Heroku:

Création app:

- `$ heroku login`
- `$ heroku create projet13-oc-lettings-site`
- `$ heroku git:remote -a projet13-oc-lettings-site`

Envoi de l'image Docker sur heroku:

- `$ heroku container:login`
- `$ heroku container:push -a projet13-oc-lettings-site web`
- `$ heroku container:release -a projet13-oc-lettings-site web`

### Intégration Continue avec CircleCI:

#### Configuration:

- création d'un dossier .circleci/ 
- fichier config.yml pour definir les actions à effectuer

#### orbs: python et heroku

#### jobs:

1. build-test-and-check

- image: python 3.10
- installation des dépendances
- effectuer les migrations
- lancement des tests unitaires (>80%)
- vérification de la conformité avec la pep8 (flake8)

2. docker-build-tag-and-push

- image: docker
- setup_remote_docker
- login docker, build image with commit hash
- tag and push to docker hub

3. deploy-to-heroku

- récupération de l'image sur docker hub
- installation d'heroku CLI et login
- docker tag and push vers heroku
- envoi sur l'app créée précédemment

#### workflows

- lancement du 1er job de tests et de vérification de conformité avec la pep8
- si, et seulement si, le 1er réussi => lancement du 2e job pour docker
- si, et seulement si, le 2e est validé => déploiement vers heroku.

A chaque push vers gitHub, circleci effectue le worflow et valide la mise à jour.

