# Automatisation des Ventes – Projet PFA

## Réalisé par

* Imen Tmar
* Tasnim Limem
* Soulayma Klai

## Encadré par

Imene Amira

## Contexte

Dans le cadre du module Logiciels, ce projet de fin d’année (PFA) a pour objectif d’automatiser l’analyse des ventes d’une entreprise e-commerce.

Face à l’augmentation du volume de données, l’utilisation d’un fichier Excel devient limitée. Ce projet propose une solution basée sur Python pour automatiser les calculs et améliorer la gestion des données.

## Objectifs du projet

* Automatiser le traitement des données de ventes
* Calculer les indicateurs financiers
* Générer automatiquement les fichiers nécessaires
* Faciliter l’analyse des performances

## Structure du projet
projet-PFA/
│── code_1.py
│── resultats_final.csv
│── README.md


## Fonctionnement

Le programme exécute automatiquement les étapes suivantes :

1. Génération du fichier `ventes.csv` via le code Python
2. Lecture des données depuis ce fichier
3. Calcul du chiffre d’affaires brut
4. Application des remises
5. Calcul du chiffre d’affaires net
6. Calcul de la TVA (20 %)
7. Calcul du chiffre d’affaires total
8. Identification du produit le plus rentable
9. Génération du fichier `resultats_final.csv`

## Données générées

Le fichier `ventes.csv` est créé automatiquement avec la structure suivante :

* ID : identifiant du produit
* Prix : prix unitaire
* Quantite : nombre d’unités vendues
* Remise : remise en pourcentage

## Formules utilisées

* CA Brut = Prix × Quantité
* CA Net = CA Brut × (1 - Remise / 100)
* TVA = CA Net × 0.20

## Exécution

1. Ouvrir le projet dans VS Code
2. Vérifier que Python est installé
3. Exécuter la commande suivante :

## Résultat

Le programme génère automatiquement :

* `ventes.csv` (données d’entrée)
* `resultats_final.csv` (résultats calculés)

Le fichier `resultats_final.csv` contient :

* Les données initiales
* CA Brut
* CA Net
* TVA

## Conclusion

Ce projet permet de mettre en pratique plusieurs notions importantes :
* Manipulation de fichiers CSV
* Automatisation avec Python
* Analyse de données
Il constitue une solution simple et efficace pour automatiser la gestion des ventes.
