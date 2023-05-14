from Joueur import Joueur
from Case import Case
from Joueur import Joueur


j=Joueur.Joueur("toto")
de = j.lance_de()
j.deplacement(28,de)
print(j.pos)
de = j.lance_de()
print(de)
j.deplacement(28,de)
print(j.pos)
de = j.lance_de()
print(de)
j.deplacement(28,de)
print(j.pos)