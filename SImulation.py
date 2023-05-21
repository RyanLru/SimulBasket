# SImulation d'une partie de basket avec 2 équipes de 5 joueurs
# Le fichier permet l'affichage graphique de la simulation


from pygame import*

import Debug
from Placement import Placement

# Initialisation de la fenêtre par une fonction
def init_fenetre():
    fenetre = display.set_mode((1820,980))
    display.set_caption("Basketball")
    return fenetre



# Fonction de boucle de jeu
def boucle_jeu(fenetre):
    # Initialisation des variables
    fond = image.load("Data/Background.jpg").convert()
    # On adapte l'image de fond à la taille de la fenêtre
    fond = transform.scale(fond,(1820,980))
    fenetre.blit(fond,(0,0))
    display.flip()
    continuer = True
    # Boucle de jeu
    while continuer:
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