# oc-litreview


## Installation et lancement du serveur

Créer un environenment virtuel avec python ou utiliser docker pour l'installation.


### Installation manuelle

Depuis la racine du projet créer un environnement virtuel
```shell
python -m venv .venv
source .venv/bin/activate
```

Puis lancer le serveur django
```shell
python src/manage.py runserver
```

Utilisez `Ctrl+C` pour stopper le serveur. 


### Installation via Docker

Il est possible de construire une image Docker si ce dernier est installé.

Depuis la racine du projet, construisez l'image avec la commande
```shell
docker-compose up
```

Puis lancer le serveur avec la commande 
```shell
docker-compose up
```

Utilisez `Ctrl+C` pour stopper le serveur. 

Pour supprimer l'image docker, utilisez la commande 
```shell
docker-compose down
```


## Accéder au site en local

Quand le serveur et lancé, le site est accessible en local sur le port par défaut de django:
http://127.0.0.1:8000/


## Interface d'administration

L'interface d'administration de django est accessible via http://127.0.0.1:8000/admin

Les identifiants administrateur sont `admin` à saisir en user et password.
