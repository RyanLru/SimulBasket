# Fichier pour afficher une Interface de Débuggage
# On utilise la bibliothèque Pygame

from pygame import*

# Initialisation de la fenêtre par une fonction
def init_fenetre():
    fenetre = display.set_mode((800,800))
    display.set_caption("Debug")
    return fenetre

# Boucle de debuggage
def boucle_debug(fenetre):
    # Initialisation des variables
    display.flip()
    continuer = True
    # Boucle de jeu
    while continuer:
        for evenement in event.get():
            if evenement.type == QUIT:
                continuer = False
        display.flip()
    quit()

# Fonction principale
def main():
    fenetre = init_fenetre()
    boucle_debug(fenetre)

main()