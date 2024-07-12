import sys

class Animal:

    def __init__(self,nom,poids,taille):
        self.__nom=nom
        #self.__poids= poids
        self.set_poids(poids)
        self.__taille= taille
    
    def __str__(self):
        return str(f"L'animal est {self.__nom}")
        pass

    """Encapsulation"""
    # getter method to get the properties using an object
    def get_nom(self):
        return  self.__nom
    
    # setter method to change the value 'a' using an object
    def set_nom(self,nom):
        self.__nom=nom

    # getter method to get the properties using an object
    def get_poids(self):
        return  self.__poids
    
    # setter method to change the value 'a' using an object
    def set_poids(self,poids):
        if poids<=0:
            raise ValueError("Entrez une valeur supérieur à 0!!!")
        else:
            self.__poids=poids

    # getter method to get the properties using an object
    def get_taille(self):
        return  self.__taille
    
    # setter method to change the value 'a' using an object
    def set_taille(self,nouvelle_taille):
        self.__taille=nouvelle_taille

def son_poids(self):
        print(f'Le poids du {self.nom} est de {self.poids} kg')    

def se_deplacer(self):
    pass

def sauter(self):
    #Appel de son_poids()
    self.son_poids()
        
    #Ne fait pas d'affichage...
    return f"Le poids pour sauter {self.poids}"   
        
class Serpent(Animal):
    def se_deplacer(self):
        print("je rampe")
        pass

class Oiseau(Animal):

    def __init__(self,__nom,__poids,__taille,altitude_max):
        
        super().__init__(__nom,__poids,__taille)
        #Autre façon de faire, Si appel de la class mère (ajouter le self)
        #Animal.__init__(self,nom,poids,taille)
        
        self.altitude= altitude_max

    def se_deplacer(self):
        print("je vole")
        pass

if __name__ == '__main__':
    #instance de la classe animal
    lion = Animal(nom='lion',poids=350,taille=154)
    #print(lion.__poids)
    print(lion.get_taille())

    #lion.sauter()

    python = Serpent('python',2,120)
    #print(f"Le {python.__nom} a un poids de {python.__poids},et une taille de {python.taille}")
    python.se_deplacer()


    aigle = Oiseau ('aigle',3,100,350)
    aigle.set_nom("aigle")
    nom_aigle= aigle.get_nom()
    print(f"Le {nom_aigle} a un poids de {aigle.get_poids()},et une taille de {aigle.get_taille()}, vole à une altitude de {aigle.altitude}")
    aigle.se_deplacer()


    lion.set_nom('lion')
    print(lion.get_nom())

    lion.set_poids(300)
    print(lion.get_poids())

    lion.set_taille(182)
    print(lion.get_taille())

    #Teste de l'exception
    """lion.set_poids(-200)
    print(lion.get_poids())"""

    print(lion.__str__())