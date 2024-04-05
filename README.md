# td_note_vueJS

### Lien Github : https://github.com/loannchhum/td_note_vueJS

## Equipe

### Developpeur 1

Ahmet BABA

### Developpeur 2

Loann CHHUM--MOXEL

## Installation et démarrage

### Création du projet avec VueJS

Afin de créer notre projet, nous avons utilisé la commande vueJS suivante :

Commande permettant de créer le projet :

```
npm create vite@latest td_note_vueJS
```

### Flask

Afin de démarrer le serveur, nous avons choisi d'utiliser flask.

Tout d'abord, il faut installer Flask :

```
pip install flask
```


Pour lancer le serveur, il suffit de se rendre dans le répertoire du projet puis dans /server et de lancer la commande :

```
flask run
```

Aussi, vous aurez certainement besoin des ajout flask suivant pour que l'ensemble des fonctionnalités soient opérationnelles.

```
pip install -U flask-cors

pip install pyyaml

pip install flask-sqlalchemy

pip install mysql-connector-python
```

### NPM


Voici les différentes commandes à exécuter afin de pouvoir installer npm qui servira à lancer notre client.

Commande permettant d'installer npm :

```
npm install
```

Commande permettant de lancer notre client npm :

```
npm run dev --host
```


### Fonctionnalités

L'application permet de gérer des questionnaires. En effet, ceux-ci peuvent contenir une ou plusieures questions.
Il existe deux types de questions, les questions simples, avec deux choix possibles et les questions multiples, avec quatre choix.

Ainsi, nous avons implémenté les fonctionnalités suivantes :

- Afficher la liste des questionnaires.
 
- Créer un questionnaire (d'abord sans questions).

- Supprimer un questionnaire.

- Modifier le nom du questionnaire.

- Accéder à la liste des questions d'un questionnaire.

- Créer une question dans un questionnaire.

- modifier une question et les choix possibles d'une question.