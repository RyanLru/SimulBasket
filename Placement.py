# Permet de gérer le placement des joueurs sur le terrain
# Placement avec différentes stratégies


def placement(equipe, sens):
    # On récupère les joueurs de l'équipe 1 et on modifie leurs coordonées en fonction du sens
    if sens == 1:
        for i in range(5):
            equipe[i].set_x(100 + i * 100)
            equipe[i].set_y(100)
    # On récupère les joueurs de l'équipe 2 et on modifie leurs coordonées en fonction du sens
    elif sens == 2:
        for i in range(5):
            equipe[i].set_x(100 + i * 100)
            equipe[i].set_y(800)
