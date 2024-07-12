from Board import Board
from Player import Player

board=Board()
board.start() 
board.liste[0][0]='X'
print(board.liste[0][0])
"""
player1 = Player(nom='J1',symbole= 'O')
player2 = Player(nom='J2',symbole= 'X')
print(f"Le joueur {player1.get_nom()} à le symbole: {player1.get_symbole()}")
print(f"Le joueur {player2.get_nom()} à le symbole: {player2.get_symbole()}")
"""

"""player = ''
if Player.first_player(player) == 1:
    player = 'X'
else:
    player='O'

print(player, f"commence")
"""
#J1 a toi de jouer (ou J2)
#While --> T[i],T[j]=T[j],T[i]
#J1=1 et J2=0 et inversement J2=1 et J1=0 /// Puis joue quand Valeur =0