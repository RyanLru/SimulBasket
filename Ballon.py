# Classe Ballon

class Ballon:

    def __int__(self):
        # coordonnées du ballon
        self.x = 0
        self.y = 0

        # vitesse du ballon
        self.vitesse = 0

        # Possession du Ballon
        self.possession = 0

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    def set_possession(self, possession):
        self.possession = possession

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vitesse(self):
        return self.vitesse

    def get_possession(self):
        return self.possession

