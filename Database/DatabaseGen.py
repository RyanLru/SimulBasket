# On Créer une base de données avec les joueurs et leurs caractéristiques avec plusieur equipes

import sqlite3

# On se connecte à la base de données
conn = sqlite3.connect('Basketball.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Joueurs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 equipe_id INTEGER,
                 nom TEXT,
                 prenom TEXT,
                 taille REAL,
                 poids REAL,
                 poste TEXT,
                 vitesse REAL,
                 agilite REAL,
                 force REAL,
                 precision REAL,
                 endurance REAL,
                 moral REAL,
                 sante REAL,
                 equipe TEXT,
                 coord_x REAL,
                 coord_y REAL,
                 coord_z REAL,
                 photo_path TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS Equipes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nom TEXT,
                 joueur_id INTEGER,
                 equipe_photo_path TEXT)''')

c.close();

