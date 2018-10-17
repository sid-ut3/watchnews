# Projet SID 2018 : WATCHNEWS
## Groupe 7 : Prédiction

*Dans le cadre du projet inter-promo 2018 de la formation SID, ce github hébergera le travail du groupe 7 en charge de la prédiction de catégories pour les articles.*


### Présentation du projet

Ce projet est réalisé sous forme de travail collaboratif entre tous les étudiants de la formation SID de l'Université Toulouse III Paul Sabatier. Les quelques 80 étudiants réunis pour l'occasion (de la L3 jusqu'au M2) travaillent en groupe pendant 2 semaines complètes début janvier et sont encadrés par une équipe d'enseignants.

Le projet WATCHNEWS consiste à la mise en place d'un site web d'analyse des médias numériques :
- Temps réel
- Analyse des tendances thématique
- Analyse sémantique des articles
- Comparaison du traitement d’un thème en fonction des sources

But : étudier les biais de traitements des différentes sources


### Présentation du groupe 7

Chef de groupe :
- Geoffrey BOLMIER

Membres du groupe :
- Noémie CRENNER
- Floric DELPUECH
- Valentin HUGUES
- Damien IZARD
- Raphaël NJAMO KAPDEM
- Cassandre OLLIVIER
- Antoine PLISSONNEAU DUQUENE
- Marianne POUCHAN
- Célia SARTORI

Notre groupe est confronté à un problème de classification : nous devons prédire les différentes catégories auxquelles appartient un article de journal. On discernera un ensemble de catégories thématiques (économie, sport, politique, etc…), et un autre ensemble de catégories sémantiques.

Tout le travail de pre-processing des textes est effectué par le groupe 5 (filtrage, pos tagging, tf-idf, etc...).

Pour les catégories thématiques nous disposons d'un dataset partiellement labellisé en multi-classe. Nous procèderons donc à un apprentissage supervisé mais nous prédirons en multi-label. Ainsi nous pourrons attribuer une ou plusieurs catégories thématiques à chaque article.

Pour les catégories sémantiques nous nous servirons des informations sémantiques (travail du groupe 6) pour créer un nouvel ensemble de catégories sémantiques par apprentissage non-supervisé.


### Gestion de projet

Nous allons utiliser différents outils agiles dédiés au bon déroulement d'un projet.

Pour communiquer nous utiliserons le logiciel Slack. C'est un outil de collaboration qui permet de travailler en groupe et en temps réel.

Nous utiliserons la platerforme GitHub pour partager notre travail. Ce réseau social dédié aux projets informatiques nous permettra de mettre en place un processus qualité. Toutes les réalisations seront versionnées et datées. Nous serons en mesure d'analyser les modifications apportées par chacun des membres du groupe.

Pour nous organiser nous utiliseront ZenHub, une application incorporable à GitHub sous forme de tableau de bord divisé en 4 parties : 
- New Issues 
- In Progress
- Done
- Closed

L'objectif étant que tous les collaborateurs puissent déterminer, visualiser et comprendre les problématiques futures, en cours et passées. Cette méthode de travail agile nous permettra de gagner du temps et d'optimiser le travail de groupe. 
