from random import randint
from Terrain import Terrain

NB_CASE = 28

class Joueur:

    def __init__(self, nom):
        self.nom = nom
        self.position = 0
        self.argent = 1500
        self.propriete = []

    def lancer_de(self):
        d1 = randint (1,6)
        d2 = randint (1,6)
        de = d1 + d2
        return de

    def deplacement(self, de):
        self.position =  (self.position + de) % NB_CASE
        return self.position

    def acheter(self, terrain):
        if self.argent > terrain.prix : 
            self.propriete.append(terrain)
            self.argent =  self.argent - terrain.prix
            print ("Votre solde est de", self.argent)
        else :
            print ("Votre solde est insuffisant")

    def payer(self, terrain, autre_joueur):
        self.terrain = terrain
        self.joueur = autre_joueur