# SImulation d'une partie de basket avec 2 équipes de 5 joueurs
# Le fichier permet l'affichage graphique de la simulation


from pygame import*
from pygame.locals import*


import Jeu
import Placement
from Ballon import Ballon

# Initialisation de la fenêtre par une fonction
def init_fenetre():
    fenetre = display.set_mode((1820,980))
    display.set_caption("Basketball")
    return fenetre

def Actualisation(fenetre, equipe1, equipe2, Balle, temps_restant, score1, score2):
    fond = image.load("Data/Background.jpg").convert()
    # On adapte l'image de fond à la taille de la fenêtre
    fond = transform.scale(fond, (1820, 980))
    fenetre.blit(fond, (0, 0))
    display.flip()

    # On affiche les joueurs en fonction de le coordonées
    for i in range(5):
        draw.circle(fenetre, (135,206,235), (equipe1[i].get_x(), equipe1[i].get_y()), 20)
        draw.circle(fenetre, (235,165,137), (equipe2[i].get_x(), equipe2[i].get_y()), 20)
    display.flip()

    # On affiche le ballon
    draw.circle(fenetre, (255,95,0), (Balle.get_x(), Balle.get_y()), 10)

    # On affiche le temps restant
    from pygame import font

    # On initialise la police
    font.init()
    font = font.Font(None, 50)
    text = font.render(str(score1)+ "  " +str(temps_restant//60)+ " : "+str(temps_restant%60)+ "  "+ str(score2), 1, (255,255,255))
    fenetre.blit(text, (820, 10))
    display.flip()

"""
    # On cherche a localiser la position des panier
    draw.circle(fenetre, (255,255,255), (200, 490), 10)
    draw.circle(fenetre, (255,255,255), (1620, 490), 10)
    display.flip()
"""


# Fonction de boucle de jeu
def boucle_jeu(fenetre):
    equipe1 = Jeu.Equipe('Golden States')
    equipe2 = Jeu.Equipe('Lakers')

    # On initialise le ballon au centre du terrain
    Balle = Ballon()
    Balle.set_x(910)
    Balle.set_y(490)

    # Compteur de temps
    temps_restant = 15*60
    score1 = 0
    score2 = 0



    Placement.placement(equipe1, 1)
    Placement.placement(equipe2, 2)

    res = Jeu.Engagement(equipe1[0], equipe2[0])

    if res == 1:
        Balle.set_possession(1)
        Balle.set_x(equipe1[0].get_x())
        Balle.set_y(equipe1[0].get_y())

    elif res == 2:
        Balle.set_possession(2)
        Balle.set_x(equipe2[0].get_x())
        Balle.set_y(equipe2[0].get_y())

    continuer = True
    # Boucle de jeu
    while continuer:
        Actualisation(fenetre, equipe1, equipe2, Balle, temps_restant,score1, score2)
        time.wait(1000)
        temps_restant -= 1
        # On affiche les joueurs
        for evenement in event.get():
            if evenement.type == QUIT:
                continuer = False

            # On récupère les coordonnées de la souris lors qu'on clique
            if evenement.type == MOUSEBUTTONDOWN:
                print(evenement.pos)

        display.flip()
    quit()

# Fonction principale
def main():
    fenetre = init_fenetre()
    boucle_jeu(fenetre)