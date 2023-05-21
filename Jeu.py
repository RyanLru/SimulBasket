# On prépare la partie et on gère les joueurs

# On Commence par créer les joueurs a partir de la classe Joueur
# On crée les joueurs de l'équipe 1
import sqlite3

from Joueurs import Joueur

def Equipe(Nomequipe):
    conn = sqlite3.connect('./Database/Basketball.db')
    c = conn.cursor()

    joueurs = []
    for i in range (10):
        # On fait une requête pour récupérer les joueurs de l'équipe 1
        c.execute("SELECT * FROM Joueurs WHERE Equipe = ? AND ID = ?", (Nomequipe, i+1))
        joueur = c.fetchone()
        if joueur is None:
            i += 1
        else:
            #print(joueur[2], " ", joueur[3], " ", joueur[4], " ", joueur[5], " ", joueur[6], " ", joueur[7], " ", joueur[8], " ", joueur[9], " ", joueur[10], " ", joueur[11], " ", joueur[12], " ", joueur[13], " ", joueur[14], " ", joueur[15], " ", joueur[16], " ", joueur[17])
            joueurs.append(Joueur(joueur[2], joueur[3], joueur[4], joueur[5], joueur[6], joueur[7], joueur[8], joueur[9], joueur[10], joueur[11], joueur[12], joueur[13], joueur[14], joueur[15], joueur[16], joueur[17]))
    conn.close()
    return joueurs

