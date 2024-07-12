from Animal import Serpent
from Animal import Oiseau
from Animal import Animal

"""Cette classe possède un attribut qui est une liste d’objets de type Animal.
Vous passerez la liste d’animaux comme paramètres lors de l’instanciation
de l’objet.

Vous définirez une méthode permettant d’ajouter un objet de type Animal à
une instance de Zoo."""

class Zoo:

    def __init__(self,list_animaux:list):
        self.list_animaux=[]
        for animal in list_animaux:
            self.ajout(animal)

    def __add__(self,other_zoo):
        return Zoo(self.list_animaux+other_zoo.list_animaux)

    def ajout(self,animal:Animal):
        if isinstance(animal, Animal):
            self.list_animaux.append(animal)
        else:
            raise TypeError('animal must be an Animal')

if __name__ == '__main__':
    lion = Animal(nom='lion',poids=350,taille=154)
    aigle = Oiseau ('aigle',3,100,350)
    python = Serpent('python',2,120)

    #V1
    list_animaux=[lion,aigle,python]
    zoo=Zoo(list_animaux)
    print(zoo)

    #V2
    #zoo=Zoo(list_animaux=[lion,aigle,python])

    chat=Animal(nom='chat',poids=2,taille=50)
    zoo.ajout(chat)
    print(zoo.list_animaux[3])

    ani=Animal(nom='girafe',poids=95,taille=450)
    zoo.ajout(ani)
    print(str(ani))

    #Nouvel animal créer dans une liste
    licorne=Animal(nom='licou',poids=200,taille=150)
    zoo2=Zoo([licorne])

    zoo3=zoo+zoo2
    zoo3=zoo.__add__(zoo2)

    for animal in zoo3.list_animaux:
        print(animal)

    lion.set_poids(250)
    print(lion.get_poids())