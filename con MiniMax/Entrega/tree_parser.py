""" 

Basado en material de Tony Poerio

Jose Cifuentes

"""
from generarArbolTest import *
from ast import literal_eval
import sys


##########################
###### PARSE DATA ########
##########################
def parse_data_as_list(fname):
	with open(fname, "r") as f:
		data_as_string = f.read()
		print (data_as_string)
		data_list = literal_eval(data_as_string)
	return data_list


class GameNode:
	def __init__(self, name, value=0, parent=None):
		self.Name = name      # a char
		self.value = value    # an int
		self.parent = parent  # a node reference
		self.children = []    # a list of nodes

	def addChild(self, childNode):
		self.children.append(childNode)

	def resumen(self):
		print("""	
					Name: {}
					Value: {}
					Parent: {}
					Children: {}

			""".format(self.Name,self.value,self.parent,self.getHijos()))
		

	def getHijos(self):
		hijos=[]
		for i in self.children:
			hijos.append(i.Name)
		return hijos


		

class GameTree:
	def __init__(self,yo):
		self.root = None
		self.YO=yo


	def build_tree(self, data_list):
		"""
		:param data_list: Take data in list format
		:return: Parse a tree from it
		"""
		self.root = GameNode(data_list.pop(0))
		for elem in data_list:
			self.parse_subtree(elem, self.root)

	def parse_subtree(self, data_list, parent):
		# base case
		if type(data_list) is tuple:
			# make connections
			leaf_node = GameNode(data_list[0])
			leaf_node.parent = parent
			parent.addChild(leaf_node)
			# if we're at a leaf, set the value
			if len(data_list) == 2:
				leaf_node.value = data_list[1]
			return

		# recursive case
		tree_node = GameNode(data_list.pop(0))
		# make connections
		tree_node.parent = parent
		parent.addChild(tree_node)
		for elem in data_list:
			self.parse_subtree(elem, tree_node)

		# return from entire method if base case and recursive case both done running
		return

	'''
	def armarSubArbol(self,value,parent,lookahead,jugador):
		if(jugador==1):
			hoja=GameNode(str(value),value)
			jugador=2
		else:
			hoja=GameNode(str(value),value*-1)
			jugador=1
		hoja.parent=parent

		parent.addChild(hoja)

		if(not (lookahead<1)):
			self.armarSubArbol(value+1,hoja,lookahead-1,jugador)
			self.armarSubArbol(value+2,hoja,lookahead-1,jugador)
			return
		return
	'''

	def armarSubArbol(self,name,value,parent,lookahead,jugador,tableroH,tableroV):

		#self.armarSubArbol(tiro,heuristica,self.root,lookahead-1,YO,tableroHNuevo.copy(),tableroVNuevo.copy())

		if(jugador==1):
			jugador=2
		else:
			jugador=1

		hoja=GameNode(str(name),value)
		hoja.parent=parent
		parent.addChild(hoja)

		if(not (lookahead<1)):
			#self.armarSubArbol(value+1,hoja,lookahead-1,jugador)
			#self.armarSubArbol(value+2,hoja,lookahead-1,jugador)



			posicionesLibresH=getPosicionesLibres(tableroH)
			posicionesLibresV=getPosicionesLibres(tableroV)

			posiblesTiros=[]

			for pos in posicionesLibresH:
				posiblesTiros.append([0,pos])

			for pos in posicionesLibresV:
				posiblesTiros.append([1,pos])


			for tiro in posiblesTiros:

				tableroHNuevo,tableroVNuevo=jugarSimulado(tableroH.copy(),tableroV.copy(),tiro,jugador)

				#print("punteo")
				heuristica=getHeuristica(tableroHNuevo.copy(),tableroVNuevo.copy(),jugador)

				self.armarSubArbol(tiro,heuristica,hoja,lookahead-1,jugador,tableroHNuevo.copy(),tableroVNuevo.copy())



			return
		return
	'''
	def armarArbol(self,rootValue,lookahead):
		self.root=GameNode(str(rootValue))

		self.armarSubArbol(rootValue+1,self.root,lookahead-1,1)
		self.armarSubArbol(rootValue+2,self.root,lookahead-1,1)
	'''
	def armarArbol(self,tableroH,tableroV,lookahead):
		self.root=GameNode("root")

		posicionesLibresH=getPosicionesLibres(tableroH)
		posicionesLibresV=getPosicionesLibres(tableroV)

		posiblesTiros=[]

		for pos in posicionesLibresH:
			posiblesTiros.append([0,pos])

		for pos in posicionesLibresV:
			posiblesTiros.append([1,pos])

		#print("YO: "+str(self.YO))
		for tiro in posiblesTiros:
			#self.armarSubArbol(rootValue+1,self.root,lookahead-1,1)
			#print()
			#print("TIRO "+str(tiro))
			tableroHNuevo,tableroVNuevo=jugarSimulado(tableroH.copy(),tableroV.copy(),tiro,self.YO)

			#print("punteo")
			heuristica=getHeuristica(tableroHNuevo.copy(),tableroVNuevo.copy(),self.YO)

			#					name,value,parent,lookahead,jugador,tableroH,tableroV
			self.armarSubArbol(tiro,heuristica,self.root,lookahead-1,self.YO,tableroHNuevo.copy(),tableroVNuevo.copy())

		


##########################
#### MAIN ENTRY POINT ####
##########################
'''
YO=1 #Jugadas positivas
OPONENTE=2 #Jugadas negativas
def main():
	#filename = sys.argv[1]
	#print ("hello world! " + filename)
	#data_list = parse_data_as_list(filename)
	data_tree = GameTree()
	
	#data_tree.build_tree(data_list)

	#armarArbol(self,tableroH,tableroV,lookahead)
	data_tree.armarArbol([99,99,99,99,99,99],[99,99, 99,99, 99,99],2)

	data_tree.root.resumen()
'''
if __name__ == "__main__":
	main()