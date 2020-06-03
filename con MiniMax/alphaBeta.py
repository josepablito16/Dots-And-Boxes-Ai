##########################
###### MINI-MAX A-B ######
##########################
import ast
class AlphaBeta:
	# print utility value of root node (assuming it is max)
	# print names of all nodes visited during search
	def __init__(self, game_tree):
		self.game_tree = game_tree  # GameTree
		self.root = game_tree.root  # GameNode
		return

	def alpha_beta_search(self, node):
		infinity = float('inf')
		best_val = -infinity
		best_name=""
		beta = infinity

		successors = self.getSuccessors(node)
		best_state = None

		for state in successors:
			value,name = self.min_value(state, best_val, beta)
			if value > best_val:
				best_val = value
				best_name=name
				best_state = state
		#print ("AlphaBeta:  Utility Value of Root Node: = " + str(best_val)+" with name "+best_name)
		#print ("AlphaBeta:  Best State is: " + best_state.Name)
		return ast.literal_eval(best_name)

	def max_value(self, node, alpha, beta):
		#print ("AlphaBeta-->MAX: Visited Node :: " + node.Name)
		if self.isTerminal(node):
			return self.getUtility(node),node.Name
		infinity = float('inf')
		value = -infinity
		name=""

		successors = self.getSuccessors(node)
		for state in successors:

			valueOfIter,nameOfIter=self.min_value(state, alpha, beta)

			if(value>valueOfIter):
				value,name=value,name
			else:
				value,name=valueOfIter,nameOfIter


			if value >= beta:
				return value,name
			alpha = max(alpha, value)
		return value,name

	def min_value(self, node, alpha, beta):
		#print ("AlphaBeta-->MIN: Visited Node :: " + node.Name)
		if self.isTerminal(node):
			return self.getUtility(node),node.Name
		infinity = float('inf')
		value = infinity
		name=""

		successors = self.getSuccessors(node)
		for state in successors:


			valueOfIter,nameOfIter=self.max_value(state, alpha, beta)

			if(value<valueOfIter):
				value,name=value,name
			else:
				value,name=valueOfIter,nameOfIter


			if value <= alpha:
				return value,name
			beta = min(beta, value)

		return value,name
	#                     #
	#   UTILITY METHODS   #
	#                     #

	# successor states in a game tree are the child nodes...
	def getSuccessors(self, node):
		assert node is not None
		return node.children

	# return true if the node has NO children (successor states)
	# return false if the node has children (successor states)
	def isTerminal(self, node):
		assert node is not None
		return len(node.children) == 0

	def getUtility(self, node):
		assert node is not None
		return node.value