+ Automatisation des Ventes – Projet PFA
  
+ Réalisé par:
  
Imen Tmar
Tasnim Limem
Soulayma Klai

+ Encadré par
Imene Amira

+ Contexte
Dans le cadre du module Logiciels, ce projet de fin d’année (PFA) a pour objectif d’automatiser l’analyse des ventes d’une entreprise e-commerce.
Face à l’augmentation du volume de données, l’utilisation d’un fichier Excel devient limitée. Ce projet propose une solution basée sur Python pour automatiser les calculs et améliorer la gestion des données.

+ Objectifs du projet
1/Automatiser le traitement des données de ventes
2/Calculer les indicateurs financiers
3/Générer automatiquement un fichier de résultats
4/Faciliter l’analyse des performances

+ Structure du projet
projet-PFA/
│── code_1.py
│── ventes.csv
│── resultats_final.csv
│── README.md

+ Données d’entrée
Le fichier ventes.csv contient les informations suivantes :
ID : identifiant du produit
Prix : prix unitaire
Quantite : nombre d’unités vendues
Remise : remise en pourcentage

+ Exemple :
ID,Prix,Quantite,Remise
101,15.0,3,10
102,25.0,2,5
103,10.0,5,0

+ Fonctionnalités:
Le programme permet de :
Lire les données depuis un fichier CSV
Calculer le chiffre d’affaires brut
Appliquer les remises
Calculer le chiffre d’affaires net
Calculer la TVA (20 %)
Calculer le chiffre d’affaires total
Identifier le produit le plus rentable
Générer un fichier resultats_final.csv

+ Formules utilisées:
CA Brut = Prix × Quantité
CA Net = CA Brut × (1 - Remise / 100)
TVA = CA Net × 0.20

+ Exécution :
Ouvrir le projet dans VS Code
Vérifier que Python est installé
Exécuter la commande suivante :
python code_1.py

+ Résultat:
Le script génère automatiquement le fichier :
resultats_final.csv
Ce fichier contient :
Les données initiales
CA Brut
CA Net
TVA

+ Conclusion:
Ce projet permet de mettre en pratique plusieurs notions importantes :
Manipulation de fichiers CSV
Automatisation avec Python
Analyse de données
Il constitue une solution simple et efficace pour améliorer la gestion des ventes
