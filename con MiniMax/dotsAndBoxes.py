import socketio
import sys
import random
from tree_parser import *
from alphaBeta import *

sio = socketio.Client()

YO=0
OPONENTE=0

class DotsAndBoxes:
	def __init__(self,username,tid):
		self.name=username
		self.tournamentId=tid
		self.playerId=0
		self.gameId=""
		self.board=[]
		

		print(self.name)
		print(self.tournamentId)

	def createBoard(self):
		self.horizontal=[

		]
		self.Vertical=[]

	def restart(self):
		self.playerId=0
		self.gameId=""
		self.board=[]
		


@sio.on('connect')
def onConnect():
    print('Connection Successfully')
    sio.emit('signin', {
        'user_name': Dot.name,
        'tournament_id': Dot.tournamentId,
        'user_role': 'player'
    })

@sio.on('ready')
def onReady(server):
    print('Ready')
    print(server)

    Dot.playerId = server['player_turn_id']
    YO=server['player_turn_id']

    if(YO==1):
        OPONENTE=2
    else:
        OPONENTE=1

    #print("Variables test")
    #print("YO: "+str(YO))
    #print("OPONENTE: "+str(OPONENTE))


    Dot.gameId = server['game_id']

    Dot.board=server['board']

    #movementType = int(input("0: Horizontal\n1: Vertical\n\t"))
    #movementIndex = int(input("0 - 29: "))
    #movementType=random.randint(0, 1)
    #movementIndex=random.randint(0, 29)


    data_tree = GameTree(int(YO))
    data_tree.armarArbol(Dot.board[0],Dot.board[1],1)

    alpha=AlphaBeta(data_tree)
    turno=alpha.alpha_beta_search(alpha.root)

    
    while int(Dot.board[turno[0]][turno[1]]) != 99:
        print("Entro al random")
    	
	
    sio.emit('play', {
        'player_turn_id': Dot.playerId,
        'tournament_id': Dot.tournamentId,
        'game_id': Dot.gameId,
        'movement': turno
    })
    print("Mando")

@sio.on('finish')
def on_finish(server):


    if (server['player_turn_id'] == server['winner_turn_id']):
        print("Win")
    else:
        print("Loose")
    
    sio.emit('player_ready', {
        'tournament_id': Dot.tournamentId,
        'game_id': Dot.gameId,
        'player_turn_id': Dot.playerId
    })
    
    Dot.restart()

#print(sys.argv)

'''
host
tid
nombre
'''

Dot=DotsAndBoxes(sys.argv[3],sys.argv[2])
sio.connect(sys.argv[1])

		
