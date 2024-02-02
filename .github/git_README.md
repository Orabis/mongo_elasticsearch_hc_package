# Documentation du Projet [Mongo-Elastic-hc-package]

## Ressource Principale

Ressources :
- [Packaging Projects Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- https://test.pypi.org/project/mongodb-elasticsearch-healthcheck-lm

---

## Étapes du Projet

### 1. Introduction

Le **Package** fournis permet de récupérer les classes `ElasticSearchCheckBackend` et `MongoDbCheckBackend`. Il est actuellement disponible sur les serveurs de tests de PyPI et sera bientôt publié globalement.

Ce dépôt GitHub sert de modèle pour d'autres packages qui pourraient être créés à l'avenir. Certains fichiers ne sont pas nécessaires pour la template :
- Le dossier `dist` (généré automatiquement, contenant le/les packages construits).
- Le dossier `.gitinfo` (contenant les informations spécifiques à ce dépôt).

#### architecture de build valide :
```
├── mongodb_elasticsearch_healthcheck
│  ├── LICENSE
│  ├── pyproject.toml
│  ├── README.md
│  ├── src
│  │  └── mongodb_elasticsearch_healthcheck_lm
│  │     ├── __init__.py
│  │     ├── elasticsearch_check.py
│  │     └── mongodb_check.py
│  └── tests
```
---
### 2. Informations Diverses 

- Assurez-vous de modifier la licence en fonction du type de droits que vous souhaitez attribuer.
- Le fichier `pyproject.toml` est le fichier principal pour la construction du package et contiendra toutes les informations nécessaires. Consultez [Comment écrire un fichier pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml) pour plus de détails.
- Le fichier `README` sera affiché comme documentation du package sur PyPI.
- J'ai rencontré des problèmes avec le backend de build `Hatchling`, j'ai donc pris `setuptools` qui fonctionne, à approfondir.
- Vous devez créer un compte sur le site PyPI et générer un token. Consultez [le fichier .pypirc (utile pour définir une configuration fixe)](https://packaging.python.org/en/latest/specifications/pypirc/).
- Pour le reste, le site fournit des explications détaillées !

---

### 3. Contact 

- Adresse e-mail : cdf.leo.merkel@gmail.com
- Léo Merkel
