import random

N = 6 #cantidad de puntos en una linea

#YO=1 #Jugadas positivas
#OPONENTE=2 #Jugadas negativas

EMPTY=99
FILLED=0

def getPosicionesLibres(lista):
	posicionesLibres=[]
	for i in range(len(lista)):
		if(lista[i]==99):
			posicionesLibres.append(i)
	return posicionesLibres
		




def buscarTiroCuadrado(tableroH,tableroV):
	posicionesLibresH=getPosicionesLibres(tableroH)
	posicionesLibresV=getPosicionesLibres(tableroV)

	posiblesTiros=[]

	for pos in posicionesLibresH:
		posiblesTiros.append([0,pos])

	for pos in posicionesLibresV:
		posiblesTiros.append([1,pos])

	#print(posiblesTiros)
	

	for turno in posiblesTiros:

		punteoAntesTurno=0
		punteoTurno=0

		acumulador = 0
		contador = 0

		for x in range(0, N * (N - 1)):
			if((x+1) % N) != 0:
				if tableroH[x] != EMPTY and tableroH[x+1] != EMPTY and tableroV[contador + acumulador] != EMPTY and tableroV[contador + acumulador + 1] != EMPTY:
					punteoAntesTurno = punteoAntesTurno + 1
					
				acumulador = acumulador + N
			else:
				contador = contador + 1
				acumulador = 0

		if(turno[0]==0):
			#Horizontal
			tableroH[turno[1]]=FILLED
		else:
			#Vertical
			tableroV[turno[1]]=FILLED


		acumulador = 0
		contador = 0

		for x in range(0, N * (N - 1)):
			if((x+1) % N) != 0:
				if tableroH[x] != EMPTY and tableroH[x+1] != EMPTY and tableroV[contador + acumulador] != EMPTY and tableroV[contador + acumulador + 1] != EMPTY:
					punteoTurno = punteoTurno + 1
					
				acumulador = acumulador + N
			else:
				contador = contador + 1
				acumulador = 0

		if(punteoAntesTurno<punteoTurno):

			#print("Cuadrado Interno")

			return turno

		else:

			if(turno[0]==0):
				#Horizontal
				tableroH[turno[1]]=EMPTY
			else:
				#Vertical
				tableroV[turno[1]]=EMPTY


	if(len(posiblesTiros)>0):
		return random.choice(posiblesTiros)
	else:
		return [0,0]


def jugarSimulado(tableroH,tableroV,turno,jugador):
	repetirTurno=True
	contador=0

	while repetirTurno:

		if(contador!=0):
			#print("Se podria simular otro tiro")
			turno=buscarTiroCuadrado(tableroH.copy(),tableroV.copy())
			#print("Turno ganador: ")
			#print(turno)
			
		else:
			contador+=1

		punteoAntesTurno=0
		punteoTurno=0

		acumulador = 0
		contador = 0

		for x in range(0, N * (N - 1)):
			if((x+1) % N) != 0:
				if tableroH[x] != EMPTY and tableroH[x+1] != EMPTY and tableroV[contador + acumulador] != EMPTY and tableroV[contador + acumulador + 1] != EMPTY:
					punteoAntesTurno = punteoAntesTurno + 1
					
				acumulador = acumulador + N
			else:
				contador = contador + 1
				acumulador = 0

		if(turno[0]==0):
			#Horizontal
			tableroH[turno[1]]=FILLED
		else:
			#Vertical
			tableroV[turno[1]]=FILLED


		acumulador = 0
		contador = 0

		for x in range(0, N * (N - 1)):
			if((x+1) % N) != 0:
				if tableroH[x] != EMPTY and tableroH[x+1] != EMPTY and tableroV[contador + acumulador] != EMPTY and tableroV[contador + acumulador + 1] != EMPTY:
					punteoTurno = punteoTurno + 1
					
				acumulador = acumulador + N
			else:
				contador = contador + 1
				acumulador = 0

		if(punteoAntesTurno<punteoTurno):
			#print()
			#print("Jugada con cuadrado")
			#print("Tablero:")
			#print([tableroH,tableroV])
			#print()
			repetirTurno=True

			if(jugador==1):
				#Positivos
				if(punteoTurno - punteoAntesTurno==1):

					if(turno[0]==0):
						#Horizontal
						tableroH[turno[1]]=1
					else:
						#Vertical
						tableroV[turno[1]]=1

				elif(punteoTurno - punteoAntesTurno==2):

					if(turno[0]==0):
						#Horizontal
						tableroH[turno[1]]=2
					else:
						#Vertical
						tableroV[turno[1]]=2

			else:
				#Negativo
				if(punteoTurno - punteoAntesTurno==1):

					if(turno[0]==0):
						#Horizontal
						tableroH[turno[1]]=-1
					else:
						#Vertical
						tableroV[turno[1]]=-1

				elif(punteoTurno - punteoAntesTurno==2):

					if(turno[0]==0):
						#Horizontal
						tableroH[turno[1]]=-2
					else:
						#Vertical
						tableroV[turno[1]]=-2
		
		else:
			repetirTurno=False

	return tableroH,tableroV

def getHeuristica(tableroH,tableroV,jugador):
	punteo=0
	if(jugador==1):
		#positivos
		#print("Es positivos")
		for i in tableroH:
			if(i!=EMPTY and i>0):
				punteo+=i

		for i in tableroV:
			if(i!=EMPTY and i>0):
				punteo+=i

		return punteo

	else:
		#Negativos
		#print("Es Negativo")
		for i in tableroH:
			if(i!=EMPTY and i<0):
				punteo+=i*-1

		for i in tableroV:
			if(i!=EMPTY and i<0):
				punteo+=i*-1
				
		return punteo


def simularMiTiro(tableroH,tableroV):


	posicionesLibresH=getPosicionesLibres(tableroH)
	posicionesLibresV=getPosicionesLibres(tableroV)

	posiblesTiros=[]

	for pos in posicionesLibresH:
		posiblesTiros.append([0,pos])

	for pos in posicionesLibresV:
		posiblesTiros.append([1,pos])

	
	for tiro in posiblesTiros:
		#print()
		#print("TIRO "+str(tiro))
		tableroHNuevo,tableroVNuevo=jugarSimulado(tableroH.copy(),tableroV.copy(),tiro,YO)
		#print([tableroHNuevo,tableroVNuevo])

		#print("punteo")
		#print(getHeuristica(tableroHNuevo.copy(),tableroVNuevo.copy(),YO))

	

############
#### MAIN ##
############
'''
h=[99, 0,0,0,0,0]
v=[99,99, 0,0, 99,0]

print()
print("SIMULAR MI TIRO")
simularMiTiro(h.copy(),v.copy())
'''