from Zoo import Zoo
from Animal import Serpent
from Animal import Oiseau
from Animal import Animal

print("zoo")
print("==============================")

#girafe= Animal()


lion = Animal(nom="lion",poids=350,taille=154)
print(lion.get_poids())
print(lion.get_taille())

#lion(350,154)

"""info_lion=lion.info()
info_lion.son[0]="miaulement"
info_lion.son"""

#Comment appeler l'héritage de Animal
python = Serpent(nom="python",poids=2,taille=120)
#print(f"poids {python.poids},et une taille de {python.taille}")


python = Serpent('python',2,120)
#print(f"Le {python.nom} a un poids de {python.poids},et une taille de {python.taille}")
python.se_deplacer()


aigle = Oiseau ('aigle',3,100,350)
nom_aigle= aigle.get_nom()
print(f"Le {nom_aigle} a un poids de {aigle.get_poids()},et une taille de {aigle.get_taille()}, vole à une altitude de {aigle.altitude}")
aigle.se_deplacer()

lion.set_nom('lion')
print(lion.get_nom())

lion.set_poids(300)
print(lion.get_poids())

print(lion.__str__())