# On code les déplacements des joueurs

# Position panier orange = (200, 490)
# Position panier bleu = (1620, 490)

# Si le joueurs possède le ballon, il va en direction du panier adverse
def direction(ballon, joueurs):
    # On regarde a qui appartient le ballon
    if ballon == 1 :
        # On déplace le joueurs en direction du panier
        joueurs.set_x(1620)
        joueurs.set_y(490)

    elif ballon == 2 :
        # On déplace le joueurs en direction du panier
        joueurs.set_x(200)
        joueurs.set_y(490)

# Si le joueur n'a pas le ballon, il va en direction du joueur qui possède le ballon

# Si le joueur n'a pas le ballon et qu'il est proche du joueur qui possède le ballon, il va en direction du panier adverse

