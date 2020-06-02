from miniMax import *
from tree_parser import *
from alphaBeta import *

#filename = sys.argv[1]
#print ("hello world! " + filename)
#data_list = parse_data_as_list(filename)


data_tree = GameTree()
#data_tree.build_tree(data_list)
data_tree.armarArbol(1,3)

mini=MiniMax(data_tree)
print("MiniMax")
bestMove=mini.minimax(mini.root)

print()
print("alpha-beta")
alpha=AlphaBeta(data_tree)
alpha.alpha_beta_search(alpha.root)
