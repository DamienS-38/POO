from information import Animal, Oiseau, Serpent

class Zoo:
    def __init__(self, animaux: list):
        self.animaux = []

        for animal in animaux:
            self.ajout_animal(animal)

    def ajout_animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.animaux.append(animal)
        else:
            raise TypeError('animal must be an Animal')

    def __add__(self, other_zoo):
        return Zoo(self.animaux + other_zoo.animaux)

if __name__ == "__main__":

    corneille = Oiseau(name = 'Cornou', weight = 0.8, size=0.35, altitude_max=500)
    lapin = Animal(name ='lapinou', weight = 1.5, size = 0.2)
    couleuvre = Serpent(name = 'nina', weight = 0.5, size = 1)
    licorne = Animal(name = 'licou', weight = 200, size = 1.5)

    zoo = Zoo(animaux = [corneille, lapin, couleuvre])
    zoo2 = Zoo([licorne])

    zoo3 = zoo + zoo2
    zoo3 = zoo.__add__(zoo2)
    for animal in zoo3.animaux:
        print(animal)