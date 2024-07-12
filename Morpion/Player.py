import random

class Player:
    
    
    def __init__(self,nom,symbole):
        self.nom=nom
        self.symbole= symbole

    
    #Objet J1 de la classe Player -> O et J2 -> X    
    
    def get_nom(self):
        return  self.nom
    
    def get_symbole(self):
        return self.symbole
    
    def first_player(self):
        return random.randint(0, 1)

        
        
    def play(self):
        pass
           

    


    
    
if __name__ == '__main__':
    player1 = Player(nom='1',symbole= 'X')
    player2 = Player(nom='',symbole= '')
    
    #print(player1.get_nom(), player1.get_symbole())
    #print(f"Le joueur {player1.get_nom()} à le symbole: {player1.get_symbole()}")
    print(player1.first_player())
    #print(player2.first_player())
    print(player1.play())