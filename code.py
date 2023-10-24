class Piece:
    def init(self, couleur):
        self.couleur = couleur

    def deplacer(self, depart, arrivee):
        # Logique générale pour le déplacement des pièces
        pass

class Pion(Piece):
    def deplacer(self, depart, arrivee):
        # Logique spécifique pour le déplacement du pion
        pass

class Tour(Piece):
    def deplacer(self, depart, arrivee):
        # Logique spécifique pour le déplacement de la tour
        pass
