# On prépare la partie et on gère les joueurs

# On Commence par créer les joueurs a partir de la classe Joueur
# On crée les joueurs de l'équipe 1
import sqlite3
import random

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


def Engagement(J1, J2):
    res = 0

    # Pourcentage de chance de gagner le duel
    stats1 = J1.get_taille()+ J1.get_poids()+ J1.get_vitesse()+ J1.get_force()+  J1.get_endurance()
    stats1 = stats1/5

    stats2 = J2.get_taille()+ J2.get_poids()+ J2.get_vitesse()+ J2.get_force()+  J2.get_endurance()
    stats2 = stats2/5

    # On transforme les stats en pourcentage
    stats1 = stats1*50 / 100
    stats2 = stats2*50 / 100

    # On calcul l'écart entre les deux joueurs cela va représenter la proba de gagner le duel pour celui qui a le plus de stats
    ecart = 1 + abs(stats1 - stats2)*10 / 100

    # On regarde qui a le plus de stats
    if stats1 > stats2:
        stats1 = stats1 * ecart
        stats2 = stats2 * 1

    elif stats1 < stats2:
        stats1 = stats1 * 1
        stats2 = stats2 * ecart


    # On calcul la proba de gagner le duel
    proba1 = stats1 / (stats1 + stats2)
    proba2 = stats2 / (stats1 + stats2)

    # On tire un nombre aléatoire entre 0 et 1
    tirage = random.random()

    # On regarde qui a gagné le duel
    if tirage < proba1:
        res = 1
        print("Le joueur ", J1.get_nom(), " ", J1.get_prenom(), " a gagné le duel contre ", J2.get_nom(), " ", J2.get_prenom(), "avec une probabilité de ", proba1)
        print("Le joueur ", J2.get_nom(), " ", J2.get_prenom(), " a perdu le duel contre ", J1.get_nom(), " ", J1.get_prenom(), "avec une probabilité de ", proba2)

    else:
        res = 2
        print("Le joueur ", J2.get_nom(), " ", J2.get_prenom(), " a gagné le duel contre ", J1.get_nom(), " ", J1.get_prenom(), "avec une probabilité de ", proba2)
        print("Le joueur ", J1.get_nom(), " ", J2.get_prenom(), " a perdu le duel contre ", J2.get_nom(), " ", J2.get_prenom(), "avec une probabilité de ", proba1)

    return res

