h=[0, 0, 99, 0, 0, 99]

v=[0, 0, 0, 99, 99, 99]

N = 3 #cantidad de puntos en una linea

posicionesLibresH=[]
def getPosicionesLibreH():
	for i in range(len(h)):
		if(h[i]==99):
			posicionesLibresH.append(i)
		
'''
def simularMiTiro():
	for i in posicionesLibresH:
		hTemp=h.copy()
		hTemp[i]=0
		print(hTemp)

print(h)
getPosicionesLibreH()
simularMiTiro()
'''


punteoTurno = 0
acumulador = 0
contador = 0
for x in range(0, N * (N - 1)):
	if((x+1) % N) != 0:
		if h[x] == 0 and h[x+1] == 0 and v[contador + acumulador] == 0 and v[contador + acumulador + 1] == 0:
			punteoTurno = punteoTurno + 1
			print("Hay cuadrado")
			h[x]=1
		
		acumulador = acumulador + N
	else:
		contador = contador + 1
		acumulador = 0

print(h)
print(v)
'''
for x in range(0, N * (N - 1)):
	if((x+1) % N) != 0:
		if h[x] == 1 and h[x+1] == 1 and v[contador + acumulador] == 1 and v[contador + acumulador + 1] == 1:
			punteoTurno = punteoTurno + 1
			print("Hay cuadrado")
		
		acumulador = acumulador + N
	else:
		contador = contador + 1
		acumulador = 0

'''
