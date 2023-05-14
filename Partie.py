from Joueur import Joueur 
from Terrain import Terrain 
from Plateau import Plateau

class Partie :
    def _init_(self,nb_joueur, joueurs) :
        self.plateau = Plateau()
        self.nb_joueur = nb_joueur
        self.joueurs = joueurs
        self.joueur_actif = joueurs[0]
        
    def choix_action(self) :
        print("Quels action souhaiter vous faire \n lancer les de (1) \n Consulter mon compte (2) \n Voir ma postion (3) ")
        reponse = int(input("Saisissez votre choix : "))
        de = 0
        while reponse != 1 :
            if reponse==1 :    
                self.deplacement()
            elif reponse==2 :
                print("Votre solde ets de :", self.joueur_actif.argent)
            else : 
                print ("Vous êtes sur la case :", self.plateau.cases[self.joueur_actif.position].nom)

    def deplacement(self) :
        de = self.joueur_actif.lancer_de() 
        self.joueur_actif.deplacement (de)
        print("Vous avez tirez : ")
        return
    
    def traitement_post_deplacement(self, case):
        # cas ou la case est depart
        #self.CaseSpeciale.carte_depart = 1
        #self.CaseSpeciale.carte_prison = 2
        #if reponse==1:
        #elif reponse==2:
        # cas ou la case est prison 
        # cas ou c'est le terrain (principal)
        self.case = case
        if self.case = terrain & terrain == achetable & self.joueur_actif.argent > terrain.prix :
            print("Voulez vous achetez ce terrain")
            reponse = int (input("OUi ou NON"))
            
            
            
               
        
    def tour(self) :
        return
        
    def joueur_faillite(self) : 
        return   
        