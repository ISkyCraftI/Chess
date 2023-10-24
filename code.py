class Piece:
    def __init__(self, couleur):
        self.couleur = couleur  # 'blanc' ou 'noir'
        self.position = None

    def deplacer(self, nouvelle_position):
        self.position = nouvelle_position

    def est_mouvement_valide(self, nouvelle_position):
        # Cette méthode doit être surchargée par chaque pièce spécifique
        raise NotImplementedError("La méthode est_mouvement_valide doit être implémentée par chaque pièce.")

class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.premier_coup = True  # Pour le déplacement initial

    def est_mouvement_valide(self, nouvelle_position):
        # Logique spécifique pour les pions
        # Ici, vous devrez vérifier que le mouvement respecte les règles des pions, comme avancer d'une case ou deux lors du premier coup.
        # Vous devrez également vérifier que le mouvement est valide par rapport à la disposition actuelle du plateau.
        raise NotImplementedError("La méthode est_mouvement_valide doit être implémentée pour le pion.")
