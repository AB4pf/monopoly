from Joueur import Joueur
from Case import Case

class Terrain(Case):
    nom=""
    def __init__(self,nom,couleur):
        self.nom=nom
        self.couleur=couleur
        self.prix=self.dico_prix[couleur][0]
        self.nu=self.dico_prix[couleur][1]
        self.maison=self.dico_prix[couleur][2]
        self.hotel=self.dico_prix[couleur][3]
        self.possede=None
        
        

