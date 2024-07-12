class Animal:
    def __init__(self, name, weight, size):
        self.name = name
        self.set_weight(weight)
        self.size = size

    def __str__(self):
        return f"Ce {self.name} a un poids de {self.get_weight()} kg et une taille de {self.size*100} cm"

    def get_weight(self):
        return self.__weight
    
    def set_weight(self, new_weight):
        # Première façon de faire en remontant des erreurs
        if not(isinstance(new_weight, int) or isinstance(new_weight, float)):
            raise TypeError("weight must be an interger or a float")
        if not (new_weight > 0):
            raise ValueError('weight doit être un nombre positif')
        
        self.__weight = new_weight

        # Deuxième façon de faire avec un try exept
        # try:
        #     if new_weight >= 0:
        #         self.__weight = new_weight
        #     else:
        #         raise ValueError
        # except ValueError:
        #     self.set_weight(abs(new_weight))


    def se_deplacer(self):
        pass


class Serpent(Animal):
    def se_deplacer(self):
        print('je rampe')

class Oiseau(Animal):
    def __init__(self, name, weight, size, altitude_max):
        super().__init__(name, weight, size)
        # Animal.__init__(self, name, weight, size) # Une autre façon de faire
        self.altitude_max = altitude_max

    def se_deplacer(self):
        print('je vole')

if __name__ == "__main__":

    chat = Animal(name = 'chat', weight = 5, size = 0.3)
    # print(chat)
    serpent = Serpent(name = 'serpent', weight = 0.5, size = 1)
    # print(serpent)
    aigle = Oiseau(name = 'aigle', weight = 3, size = 0.9, altitude_max=6000)
    # chat.se_deplacer()
    # serpent.se_deplacer()
    # aigle.se_deplacer()
    # print(aigle.altitude_max)
    print(aigle)
    aigle.set_weight(5)
    print(aigle)