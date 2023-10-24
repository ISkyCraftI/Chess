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
        x1, y1 = self.position
        x2, y2 = nouvelle_position

        # Les pions se déplacent en avant d'une case (ou de deux au premier coup)
        if self.couleur == 'blanc':
            direction = 1  # Les pions blancs avancent vers le haut du plateau
        else:
            direction = -1  # Les pions noirs avancent vers le bas du plateau

        if self.premier_coup and y2 == y1 + 2 * direction:
            return True  # Premier coup, peut avancer de deux cases
        elif y2 == y1 + direction:
            return True  # Avancer d'une case

        return False  # Mouvement invalide

class Plateau:
    length = ['A','B','C','D','E','F','G','H']  # horizontal du plateau
    width = ['1','2','3','4','5','6','7','8']   # vertical du plateau
    first_init = [[None for i in range (9)]None for i in range (9)]
    def __init__(self, length, width):
        self.length = length
        self.width = width

    

# Exemple d'utilisation :
pion_blanc = Pion('blanc')
pion_blanc.deplacer((1, 2))  # Déplacer le pion blanc à la position (1, 2)
print(pion_blanc.est_mouvement_valide((1, 3)))  # Doit renvoyer True pour un mouvement valide
print(pion_blanc.est_mouvement_valide((1, 4)))  # Doit renvoyer True pour un mouvement valide au premier coup
print(pion_blanc.est_mouvement_valide((1, 5)))  # Doit renvoyer False, mouvement invalide
