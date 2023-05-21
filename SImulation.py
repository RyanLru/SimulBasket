# SImulation d'une partie de basket avec 2 équipes de 5 joueurs
# Le fichier permet l'affichage graphique de la simulation


from pygame import*

import Jeu
import Placement

# Initialisation de la fenêtre par une fonction
def init_fenetre():
    fenetre = display.set_mode((1820,980))
    display.set_caption("Basketball")
    return fenetre

def Actualisation(fenetre, equipe1, equipe2):
    # On affiche les joueurs en fonction de le coordonées
    for i in range(5):
        draw.circle(fenetre, (255, 255, 255), (equipe1[i].get_x(), equipe1[i].get_y()), 20)
        draw.circle(fenetre, (255, 255, 255), (equipe2[i].get_x(), equipe2[i].get_y()), 20)
    display.flip()


# Fonction de boucle de jeu
def boucle_jeu(fenetre):
    equipe1 = Jeu.Equipe('Golden States')
    equipe2 = Jeu.Equipe('Lakers')

    Placement.placement(equipe1, 1)
    Placement.placement(equipe2, 2)

    # Initialisation des variables
    fond = image.load("Data/Background.jpg").convert()
    # On adapte l'image de fond à la taille de la fenêtre
    fond = transform.scale(fond,(1820,980))
    fenetre.blit(fond,(0,0))
    display.flip()
    continuer = True
    # Boucle de jeu
    while continuer:
        Actualisation(fenetre, equipe1, equipe2)
        # On affiche les joueurs
        for evenement in event.get():
            if evenement.type == QUIT:
                continuer = False
        display.flip()
    quit()

# Fonction principale
def main():
    fenetre = init_fenetre()
    boucle_jeu(fenetre)

main()