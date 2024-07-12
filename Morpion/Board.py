from Player import Player
import random

class Board:
    def __init__(self):
        self.liste=[]
        self.draw()

    
    
    def draw(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append('-')
            self.liste.append(row)

    def show_board(self):
        for row in self.liste:
            for i in row:
                print(i, end='')
            print()

    def start(self):
        self.player1 = Player('Joueur 1', 'X')
        self.player2 = Player('Joueur 2', 'O')
        l = [self.player1, self.player2]
        self.active_player = random.choice(l)

        print(self.active_player.nom, f" commence")
        self.show_board() 
        
        while board.win_condition() == False:
            board.mettre_valeur()
            board.show_board()  

            board.win_condition()
            board.swap()
            print(f"{self.active_player.nom} a toi de jouer")
        print(f"{self.active_player.nom} à gagné")
    
    
    def mettre_valeur(self):
        row= int(input("quelle ligne (1 à 3)? ")) -1

        col=int(input("quelle colonne (1 à 3)? ")) -1
        self.liste[col][row] = self.active_player.symbole
    
    #Changement de joueur
    def swap(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
        
    #Méthode pour mettre une valeur dans la liste
    def play(self, row, col,player):
        self.liste[row][col]=player
        #print(player)



    def win_condition(self):
        victoire = False
       
        #for i, j in range (3):
        if board.liste[0][0] == 'X' and board.liste[0][1] == 'X' and board.liste[0][2] == 'X' or board.liste[0][0] == 'O' and board.liste[0][1] == 'O' and board.liste[0][2] == 'O':
            victoire = True
        elif board.liste[1][0] == 'X' and board.liste[1][1] == 'X' and board.liste[1][2] == 'X' or board.liste[1][0] == 'O' and board.liste[1][1] == 'O' and board.liste[1][2] == 'O':
            victoire = True
        elif board.liste[2][0] == 'X' and board.liste[2][1] == 'X' and board.liste[2][2] == 'X' or board.liste[2][0] == 'O' and board.liste[2][1] == 'O' and board.liste[2][2] == 'O':
            victoire = True
        elif board.liste[0][0] == 'X' and board.liste[1][0] == 'X' and board.liste[2][0] == 'X' or board.liste[0][0] == 'O' and board.liste[1][0] == 'O' and board.liste[2][0] == 'O':
            victoire = True
        elif board.liste[0][1] =='X' and board.liste[1][1] == 'X' and board.liste[2][1] == 'X' or board.liste[0][1] == 'O' and board.liste[1][1] == 'O' and board.liste[2][1] == 'O':
            victoire = True
        elif board.liste[0][2] == 'X' and board.liste[1][2] == 'X' and board.liste[2][2] == 'X' or board.liste[0][2] == 'O' and board.liste[1][2] == 'O' and board.liste[2][2] == 'O':
            victoire = True
        elif board.liste[0][0] == 'X' and board.liste[1][1] == 'X' and board.liste[2][2] == 'X' or board.liste[0][0] == 'O' and board.liste[1][1] == 'O' and board.liste[2][2] =='O':
            victoire = True
        elif board.liste[2][0] == 'X' and board.liste[1][1] == 'X' and board.liste[0][2] == 'X' or board.liste[2][0] == 'O' and board.liste[1][1] == 'O' and board.liste[0][2] == 'O':
            victoire = True
        return victoire
        




    def match_nul(self):
        #Si toute la liste rempli = match nul
        i = (len(board.liste[0]))
        print(i)
        for j in range(i):
            for k in range(i):
                if board.liste[j][k] !="-":
                    print('Match nul')
                    break
                else:   
                    print('Continuer')

if __name__ == '__main__':
    board=Board()
    board.start()  

    #boucle qui va de 0,0 à 2,2
    
    #board.liste[0][0]=board.player
    """print(board.liste[0][0])
    print(board.liste[2][2])"""

    
    
    
#row, col = list(map(int, input("Enter row and column numbers to fix spot : ").split()))
    
