*Projet de Fin d’Année : Automatisation des Ventes
*Réalisé par:
imen tmar,tasnim limem,soulayma klaii
*Matière:
logiciel
*Objectif
Ce projet consiste à automatiser l’analyse des ventes d’une entreprise e-commerce à l’aide de Python, afin de remplacer l’utilisation d’un fichier Excel devenu trop volumineux.
*Structure du projet
projet-PFA/
│── code_1.py
│── ventes.csv
│── resultats_final.csv
│── README.md

*Données d’entrée
Le fichier 'ventes.csv' contient les colonnes suivantes :
-ID : identifiant du produit
-Prix : prix unitaire
-Quantite : nombre d’unités vendues
-Remise : réduction en pourcentage

*Exemple :
ID,Prix,Quantite,Remise
101,15.0,3,10
102,25.0,2,5
103,10.0,5,0

*Fonctionnalités
Le script Python permet de :
Lire les données depuis un fichier CSV
Calculer le chiffre d’affaires brut (CA Brut)
Appliquer la remise (%)
Calculer le chiffre d’affaires net (CA Net)
Calculer la TVA (20%)
Calculer le chiffre d’affaires total
Identifier le produit le plus rentable
Générer un fichier 'resultats_final.csv'

*Formules utilisées:
CA Brut= Prix × Quantité
CA Net= CA Brut × (1 - Remise / 100)
TVA= CA Net × 0.20
*Exécution du projet

1. Ouvrir le projet dans VS Code
2. Vérifier que Python est installé
3. Exécuter le script

*Résultat:
Le programme génère un fichier 'resultats_final.csv'contenant :
Les données initiales
CA Brut
CA Net
TVA


---
