# Bot Discord - Échecs

Ce projet a été réalisé par une équipe de 4 collaborateurs dans le cadre de notre formation.  
L’objectif était de concevoir un bot Discord capable de faire jouer des parties d’échecs entre utilisateurs d’un serveur, ou contre une intelligence artificielle.

Le sujet était le suivant :

---

## Objectifs du projet

L’idée principale était de permettre à n’importe quel utilisateur d’un serveur Discord de :
- Lancer une partie d’échecs contre un autre joueur ou contre une IA
- Effectuer des coups directement via des commandes textuelles
- Visualiser l’état du plateau
- Recevoir des retours clairs du bot, et retrouver une partie en cours

Le bot devait également proposer une base de données pour stocker les parties et respecter des règles précises de structuration du code (POO, typage, commentaires…).

---

## Fonctionnalités développées

- Jeu en ligne par commandes Discord
- Mode 1v1 entre utilisateurs
- Mode joueur vs IA :
  - IA "Random" (joue des coups valides au hasard, peut mater si possible)
  - IA "Algo" (basée sur un algorithme de type MinMax ou simplifié)
- Sauvegarde des parties en base SQL
- Reprise de parties incomplètes
- Commande `!help` pour afficher la liste des fonctionnalités

---

## Technologies utilisées

- Python 3.10
- discord.py
- SQLite (ou MySQL en fonction de l’environnement)
- Programmation orientée objet
- Code typé et commenté

---

## Commandes disponibles

- `!start` : démarre une nouvelle partie
- `!move e2e4` : effectue un coup
- `!board` : affiche l’état actuel du plateau
- `!resign` : permet de quitter une partie
- `!help` : affiche l’aide

---

## Structure du projet

Le projet est structuré en plusieurs modules pour rester clair et maintenable :

- `bot.py` : gestion des interactions Discord
- `chess_engine/` : moteur de jeu (validation des règles, IA, déplacements)
- `commands/` : traitement des commandes utilisateur
- `models/` : classes représentant les joueurs, parties, et échiquier
- `db/` : gestion des connexions SQL et requêtes associées

---

## Lancement du projet

1. Cloner le dépôt :

```bash
git clone https://github.com/ton-utilisateur/echec-discord-bot.git
cd echec-discord-bot
