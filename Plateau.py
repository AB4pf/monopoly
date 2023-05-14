from Terrain import Terrain

class Plateau:

    def __init__(self):
        self.cases=[]

        # self.cases Marron
        Boulevard_de_Belleville=Terrain("Boulevard de Belleville","Marron")
        Rue_Lecourbe=Terrain("Rue Lecourbe","Marron")
        self.cases.append(Boulevard_de_Belleville)
        self.cases.append(Rue_Lecourbe)

        # self.cases Bleu
        Rue_de_Vaugirard=Terrain("Rue de Vaugirard","Bleu")
        Rue_de_courcelles=Terrain("Rue de courcelles","Bleu")
        Avenue_de_la_Republique=Terrain("Avenue de la Republique","Bleu")
        self.cases.append(Rue_de_Vaugirard)
        self.cases.append(Rue_de_courcelles)
        self.cases.append(Avenue_de_la_Republique)

        # self.cases Rose
        Boulevard_de_la_Villette=Terrain("Boulevard_de_la_Villette","Rose")
        Avenue_de_Neuilly=Terrain("Avenue de Neuilly","Rose")
        Rue_de_Paradis=Terrain("Rue de Paradis","Rose")
        self.cases.append(Boulevard_de_la_Villette)
        self.cases.append(Avenue_de_Neuilly)
        self.cases.append(Rue_de_Paradis)

        # self.cases Orange
        Avenue_de_Mozart=Terrain("Avenue de Mozart","Orange")
        Boulevard_Saint_Michel=Terrain("Boulevard Saint-Michel","Orange")
        Place_Pigalle=Terrain("Place Pigalle","Orange")
        self.cases.append(Avenue_de_Mozart)
        self.cases.append(Boulevard_Saint_Michel)
        self.cases.append(Place_Pigalle)

         # self.cases Rouge
        Avenue_Matignon=Terrain("Avenue Matignon","Rouge")
        Boulevard_Malesherbes=Terrain("Boulevard Malesherbes","Rouge")
        Avenue_Henry_Martin=Terrain("Avenue Henry Martin","Rouge")
        self.cases.append(Avenue_Matignon)
        self.cases.append(Boulevard_Malesherbes)
        self.cases.append(Avenue_Henry_Martin)

        # self.cases Jaune
        Faubourg_Saint_Honoré=Terrain("Faubourg Saint-Honoré","Jaune")
        Place_de_la_Bourse=Terrain("Place de la Bourse","Jaune")
        Rue_la_Fayette=Terrain("Rue la Fayette","Jaune")
        self.cases.append(Faubourg_Saint_Honoré)
        self.cases.append(Place_de_la_Bourse)
        self.cases.append(Rue_la_Fayette)

        # self.cases Vert
        Avenue_de_Breteuil=Terrain("Avenue de Breteuil","Vert")
        Avenue_Foch=Terrain("Avenue Foch","Vert")
        Boulevard_Capucines=Terrain("Boulevard Capucines","Vert")
        self.cases.append(Avenue_de_Breteuil)
        self.cases.append(Avenue_Foch)
        self.cases.append(Boulevard_Capucines)

        # self.cases Violet
        Avenue_des_Champs=Terrain("Avenue des Champs","Violet")
        Rue_de_la_Paix=Terrain("Rue_de_la_Paix","Violet")
        self.cases.append(Avenue_des_Champs)
        self.cases.append(Rue_de_la_Paix)