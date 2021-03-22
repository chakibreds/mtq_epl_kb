# Base de connaissance sur la première league.

Il est demandé, pour un domaine applicatif, de proposer une illustration de mise en œuvre des techniques et technologies de l’[Ingénierie des Connaissances](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie_des_connaissances).

Le domaine applicatif, ici traiter, est le [pari sportif](https://fr.wikipedia.org/wiki/Pari_sportif). L'objectif est de définir une base de connaissance qui permettra de classer des matches de football en plusieurs niveaux de risques et d'exécuter sur cette dernière des requêtes [SPARQL](https://fr.wikipedia.org/wiki/SPARQL)/[DL](https://fr.wikipedia.org/wiki/Logique_de_description) afin de trouver les équipes pour lesquelles parier avec un risque le plus faible possible.

## Modélisation

Pour des détails sur la partie modélisation du projet, veuillez voir le [rapport](./rapport/rapport.pdf).

## Implémentation

### Dépendances

#### Python

Pour installer les dépendances associé au code python, exécuter cette commande 
```
pip3 install -r requirements.txt
```

#### Jena

L'API Jena utilisée est directement incluse dans le projet sous `src/reasoner/lib/`

### Ontologies

L'implémentation de le T-Box et la A-Box  est réalisée à partir de l’outil [Protégé](https://fr.wikipedia.org/wiki/Prot%C3%A9g%C3%A9_(logiciel)). Les ontologies sont dans le dossier [ontologies](./ontologies).

## Utilisation

Dans le dossier `src/`:
```
cd src/
```

Exéuter les deux scripts python suivants:

```
# pour charger les données
python3 main.py
# Pour exécuter les requêtes finales
python3 query.py
```

## Auteurs

- Elhouiti Chakib -> celhouiti@gmail.com
- Kezzoul Massili -> massy.kezzoul@gmail.com
- Bouzidi Belkassim -> bouzidi.belkassim@etu.umontpellier.fr