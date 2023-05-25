# Permet de gérer le placement des joueurs sur le terrain
# Placement avec différentes stratégies


def placement(equipe, sens):
    # On récupère les joueurs de l'équipe 1 et on modifie leurs coordonées en fonction du sens
    if sens == 1:
        equipe[0].set_x(880)
        equipe[0].set_y(490)


    # On récupère les joueurs de l'équipe 2 et on modifie leurs coordonées en fonction du sens
    elif sens == 2:
        for i in range(5):
            equipe[0].set_x(945)
            equipe[0].set_y(490)
