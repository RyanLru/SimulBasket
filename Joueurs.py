# Classe pour un Joueur

class Joueur:

    def __init__(self, nom, prenom, taille, poids, poste, vitesse, agilite, force, precision, endurance, moral, sante, equipe, x, y, z):

        # Attributs principaux
        self.nom = nom
        self.prenom = prenom
        self.taille = taille
        self.poids = poids
        self.poste = poste
        self.vitesse = float(vitesse)
        self.agilite = float(agilite)
        self.force = float(force)
        self.precision = float(precision)
        self.endurance = float(endurance)
        self.moral = float(moral)
        self.sante = float(sante)
        self.equipe = equipe

        # Attributs secondaires
        self.vitesse_moyenne = (self.vitesse + self.agilite) / 2
        self.precision_moyenne = (self.precision + self.agilite) / 2
        self.endurance_moyenne = (self.endurance + self.force) / 2
        self.moral_moyen = (self.moral + self.sante) / 2

        # Attributs de jeu
        self.score = 0
        self.passe = 0
        self.rebond = 0
        self.interception = 0
        self.contre = 0
        self.faute = 0
        self.faute_technique = 0
        self.faute_flagrante = 0
        self.perte_de_balle = 0
        self.tir_a_2_points = 0
        self.tir_a_3_points = 0
        self.tir_a_2_points_reussi = 0
        self.tir_a_3_points_reussi = 0

        # Position du joueur sur le terrain
        self.x = x
        self.y = y
        self.z = z




    # Setters
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    # Getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z



