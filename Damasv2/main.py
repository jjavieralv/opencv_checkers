import array
import numpy as np
#las funciones validar comer comprueban si la pieza tiene opción a comer 
class movimiento:
		#Peones
	def validarComerDe(tablero,color,x,y):
		if (color == "negro" and ((x+2)<=7 and (y+2)<=7)):
			if (tablero[x+1][y+1] == 1 or tablero[x+1][y+1] == 2):
				if tablero[x+2][y+2] == 0:
					return True
		if (color == "blanco" and ((x-2)>=0 and (y+2)<=7)):
			if tablero[x-1][y+1] == 3 or tablero[x-1][y+1] == 4:
				if tablero[x-2][y+2] == 0:
					return True
		return False

	def comerDe(tablero,color,x,y):
		tableroActual = tablero.copy()
		if(color=="blanco"):
			tableroActual[x][y] = 0
			tableroActual[x-1][y+1]=0
			tableroActual[x-2][y+2]=1
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x-2,y+2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x-2,y+2)
			elif(movimiento.validarComerIz(tableroActual,color,x-2,y+2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x-2,y+2)
			if(Tablero.esDama(x-2,y+2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-2,y+2,color)
		else:
			tableroActual[x][y]=0
			tableroActual[x+1][y+1]=0
			tableroActual[x+2][y+2]=3
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x+2,y+2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x+2,y+2)
			elif(movimiento.validarComerIz(tableroActual,color,x+2,y+2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x+2,y+2)
			if(Tablero.esDama(x+2,y+2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+2,y+2,color)

		return nextTablero

	def validarComerDeInv(tablero,color,x,y):
		if (color == "negro" and (x-2>=0 and y+2<=7)):
			if tablero[x-1][y+1] == 1 or tablero[x-1][y+1] == 2:
				if tablero[x-2][y+2] == 0:
					return True
		if (color == "blanco" and ((x+2)<=0 and (y+2)<=7)): 
			if tablero[x+1][y+1] == 3 or tablero[x+1][y+1] == 4:
				if tablero[x+2][y+2] == 0:
					return True
		return False

	def comerDeInv(tablero,color,x,y):
		tableroActual = tablero.copy()
		if(color=="negro"):
			tableroActual[x][y] = 0
			tableroActual[x-1][y+1]=0
			tableroActual[x-2][y+2]=3
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x-2,y+2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x-2,y+2)
			elif(movimiento.validarComerIz(tableroActual,color,x-2,y+2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x-2,y+2)
			if(Tablero.esDama(x-2,y+2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-2,y+2,color)
		else:
			tableroActual[x][y]=0
			tableroActual[x+1][y+1]=0
			tableroActual[x+2][y+2]=1
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x+2,y+2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x+2,y+2)
			elif(movimiento.validarComerIz(tableroActual,color,x+2,y+2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x+2,y+2)
			if(Tablero.esDama(x+2,y+2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+2,y+2,color)

		return tableroActual


	def validarComerIz(tablero,color,x,y):
		
		if color == "negro" and (x+2<=7 and y-2>=0):
			if tablero[x+1][y-1] == 1 or tablero[x+1][y-1] == 2:
				if tablero[x+2][y-2] == 0:
					return True
		if color == "blanco" and (x-2>=0 and y-2>=0):
			if tablero[x-1][y-1] == 3 or tablero[x-1][y-1] == 4:
				if tablero[x-2][y-2] == 0:
					return True
		return False

	def comerIz(tablero,color,x,y):
		tableroActual = tablero.copy()
		if(color=="blanco"):
			tableroActual[x][y]=0
			tableroActual[x-1][y-1]=0
			tableroActual[x-2][y-2]=1
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x-2,y-2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x-2,y-2)
			elif(movimiento.validarComerIz(tableroActual,color,x-2,y-2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x-2,y-2)
			if(Tablero.esDama(x-2,y-2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-2,y-2,color)

		else:
			tableroActual[x][y]=0
			tableroActual[x+1][y-1]=0
			tableroActual[x+2][y-2]=3
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x+2,y-2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x+2,y-2)
			elif(movimiento.validarComerIz(tableroActual,color,x+2,y-2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x+2,y-2)
			if(Tablero.esDama(x+2,y-2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+2,y-2,color)

		return nextTablero

	def validarComerIzInv(tablero,color,x,y):

		if color == "negro" and (x-2>=0 and y-2>=0):
			if tablero[x-1][y-1] == 1 or tablero[x-1][y-1] == 2:
				if tablero[x-2][y-2] == 0:
					return True
		if color == "negro" and (x+2<=7 and y-2>=0):
			if tablero[x+1][y-1] == 3 or tablero[x+1][y-1] == 4:
				if tablero[x+2][y-2] == 0:
					return True
		return False

	def comerIzInv(tablero,color,x,y):
		tableroActual = tablero.copy()
		if(color=="negro"):
			tableroActual[x][y]=0
			tableroActual[x-1][y-1]=0
			tableroActual[x-2][y-2]=3
			nextTablero = tableroActual
			if(movimiento.validarComerDeInv(tableroActual,color,x-2,y-2)):
				nextTablero = movimiento.comerDeInv(tableroActual,color,x-2,y-2)
			elif(movimiento.validarComerIz(tableroActual,color,x-2,y-2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x-2,y-2)
			if(Tablero.esDama(x-2,y-2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-2,y-2,color)
		else:
			tableroActual[x][y]=0
			tableroActual[x+1][y-1]=0
			tableroActual[x+2][y-2]=1
			nextTablero = tableroActual
			if(movimiento.validarComerDe(tableroActual,color,x+2,y-2)):
				nextTablero = movimiento.comerDe(tableroActual,color,x+2,y-2)
			elif(movimiento.validarComerIz(tableroActual,color,x+2,y-2)):
				nextTablero =  movimiento.comerIz(tableroActual,color,x+2,y-2)
			if(Tablero.esDama(x+2,y-2,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+2,y-2,color)

		return tableroActual

		#Dama
	def validarComerDamaDeU(tablero,color,x,y):
		x1=x, y1=y
		if color == "negro":
			while(y1<8):
				if(validarComerDe(tablero,"negro",x1,y1)):
					return True
				y1+=1
				x1+=1
			return False
		else:
			while(y1<8):
				if(validarComerDe(tablero,"blanco",x1,y1)):
					return True
				y1+=1
				x1-=1
			return False
	def comerDamaDeU(tablero,color,x,y):
		tableroActual = tablero.copy()
		x1=x, y1=y
		if color == "negro":
			while(y1<8):
				if(validarComerDe(tableroActual,"negro",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1+1][y1+1]=0
					tableroActual[x1+2][y1+2]=4
				y1+=1
				x1+=1
		else:
			while(y1>=0):
				if(validarComerDe(tablero,"blanco",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1-1][y1+1]=0
					tableroActual[x1-2][y1+2]=2
				y1+=1
				x1-=1
		return tableroActual

	def validarComerDamaDeD(tablero,color,x,y):
		x1=x, y1=y
		if color == "negro":
			while(y1<8):
				if(validarComerDeInv(tablero,"negro",x1,y1)):
					return True
				y1+=1
				x1-=1
			return False
		else:
			while(y1>=0):
				if(validarComerDeInv(tablero,"blanco",x1,y1)):
					return True
				y1+=1
				x1+=1
			return False

	def comerDamaDeU(tablero,color,x,y):
		tableroActual = tablero.copy()
		x1=x, y1=y
		if color == "blanco":
			while(y1<8):
				if(validarComerDeInv(tableroActual,"blanco",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1+1][y1+1]=0
					tableroActual[x1+2][y1+2]=2
				y1+=1
				x1-=1
		else:
			while(y1>=0):
				if(validarComerDeInv(tablero,"negro",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1-1][y1+1]=0
					tableroActual[x1-2][y1+2]=4
				y1+=1
				x1+=1
		return tableroActual

	def validarComerDamaIzU(tablero,color,x,y):
		x1=x, y1=y
		if color == "negro":
			while(y1>=0):
				if(validarComerIz(tablero,"blanco",x1,y1)):
					return True
					break
				y1-=1
				x1+=1
			return False
		else:
			while(y1>=0):
				if(validarComerIz(tablero,"blanco",x1,y1)):
					return True
					break
				y1-=1
				x1-=1
			return False

	def comerDamaIzU(tablero,color,x,y):
		tableroActual = tablero.copy()
		x1=x, y1=y
		if color == "negro":
			while(y1>=0):
				if(validarComerIz(tableroActual,"negro",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1+1][y1-1]=0
					tableroActual[x1+2][y1-2]=4
				y1-=1
				x1+=1
		else:
			while(y1>=0):
				if(validarComerIz(tablero,"blanco",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1-1][y1-1]=0
					tableroActual[x1-2][y1-2]=2
				y1-=1
				x1-=1
		return tableroActual

	def validarComerDamaIzD(tablero,color,x,y):
		x1=x, y1=y
		if color == "negro":
			while(y1>=0):
				if(validarComerIzInv(tablero,"negro",x1,y1)):
					return True
					break
				y1-=1
				x1-=1
			return False
		else:
			while(y1>=0):
				if(validarComerIzInv(tablero,"blanco",x1,y1)):
					return True
					break
				y1-=1
				x1+=1
			return False
		
	def comerDamaIzD(tablero,color,x,y):
		tableroActual = tablero.copy()
		x1=x, y1=y
		if color == "blanco":
			while(y1>=8):
				if(validarComerDeInv(tableroActual,"blanco",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1+1][y1-1]=0
					tableroActual[x1+2][y1-2]=2
				y1-=1
				x1-=1
		else:
			while(y1>=0):
				if(validarComerDeInv(tablero,"negro",x1,y1)):
					tableroActual[x][y]=0
					tableroActual[x1-1][y1-1]=0
					tableroActual[x1-2][y1-2]=4
				y1-=1
				x1+=1
		return tableroActual
			 		
	#Validar movimiento

	def validarMovDe(tablero,color,x,y):

		if color == "negro" and (x+1<7 and y+1<7):
			if tablero[x+1][y+1] == 0:
				return True
		if color == "blanco" and (x-1>=0 and y+1<7): 
			if tablero[x-1][y+1] == 0:
				return True
		return False

	def moverDe(tablero,color,x,y):
		nextTablero = tablero.copy()
		if(color=="blanco"):
			nextTablero[x-1][y+1]=nextTablero[x][y]
			nextTablero[x][y]=0
			if(Tablero.esDama(x-1,y+1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-1,y+1,color)
		else:
			nextTablero[x+1][y+1] = nextTablero[x+1][y+1]
			nextTablero[x][y]=0
			if(Tablero.esDama(x+1,y+1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+1,y+1,color)

		return nextTablero

	def validarMovDeInv(tablero,color,x,y):
		if color == "negro" and (x-1>=0 and y+1<=7):
			if tablero[x-1][y+1] == 0:
				return True
		if color == "blanco" and (x+1>=0 and y+1<=7):
			if tablero[x+1][y+1] == 0:
				return True
		return False

	def moverDeInv(tablero,color,x,y):
		nextTablero = tablero.copy()
		if(color=="negro"):
			nextTablero[x-1][y+1] = nextTablero[x][y]
			nextTablero[x][y]=0
			if(Tablero.esDama(x-1,y+1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-1,y+1,color)
		else:
			nextTablero[x+1][y+1]= nextTablero[x][y]
			nextTablero[x][y]=0
			if(Tablero.esDama(x+1,y+1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+1,y+1,color)
		return nextTablero

	def validarMovIz(tablero,color,x,y):
		if color == "negro" and (x+1<=7 and y-1>=0):
			if tablero[x+1][y-1] == 0:
				return True
		if color == "blanco" and (x-1>=0 and y-1>=0):
			if tablero[x-1][y-1] == 0:
				return True
		return False

	def moverIz(tablero,color,x,y):
		nextTablero = tablero.copy()
		if(color=="blanco"):
			nextTablero[x-1][y-1] = nextTablero[x][y]
			nextTablero[x][y]=0
			if(Tablero.esDama(x-1,y-1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-1,y-1,color)
		else:
			nextTablero[x+1][y-1] = nextTablero[x][y]
			nextTablero[x][y]=0
			if(Tablero.esDama(x+1,y-1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-1,y-1,color)
		return nextTablero


	def validarMovIzInv(tablero,color,x,y):
		if (x-1<6 or y-1>0):
			if color == "negro":
				if tablero[x-1][y-1] == 0:
					return True
			else: 
				if tablero[x+1][y-1] == 0:
					return True
		return False

	def moverIzInv(tablero,color,x,y):
		nextTablero = tablero.copy()
		if(color=="negro"):
			nextTablero[x-1][y-1]= nextTablero[x+1][y+1]
			nextTablero[x][y]=0
			if(Tablero.esDama(x-1,y-1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x-1,y-1,color)
			
		else:
			nextTablero[x+1][y-1]=nextTablero[x+1][y+1]
			nextTablero[x][y]=0
			if(Tablero.esDama(x+1,y-1,color)):
				nextTablero=Tablero.convertirEnDama(nextTablero,x+1,y-1,color)
		return nextTablero



class Tablero:

	def generarTablero():
		tablero = np.zeros((8,8))

		for i in range(3):
			if (i %2 != 0):
				for j in range(8):
					if (j %2 == 0):
						tablero[i][j]=0
					else:
						tablero[i][j]=3
			else:
				for j in range(8):
					if (j %2 != 0):
						tablero[i][j]=0
					else:
						tablero[i][j]=3
		for i in range(3,4):
			for j in range(0,7):
				tablero[i][j]=0

		for i in range(5,8):
			if (i %2 != 0):
				for j in range(8):
					if (j %2 == 0):
						tablero[i][j]=0
					else:
						tablero[i][j]=1
			else:
				for j in range(8):
					if (j %2 != 0):
						tablero[i][j]=0
					else:
						tablero[i][j]=1
		return tablero

	def setMejorTablero(tablero):
		global mejorTablero
		mejorTablero = tablero.copy()

	def invertirColor(color):
		if (color == "blanco"):
			return "negro"
		else:
			return "blanco"

	def minimax(tablero,color):
		x = Tablero.contarFichas(tablero,color)
		y = Tablero.contarFichas(tablero,Tablero.invertirColor(color))

		return x-y


	def esDama(x,y,color):
		#Se puede llamar directamente a la función convertirEnDama desde aquí
		#para blanca
		if(color == "blanco" and x == 0):
			return True

		#para negra
		elif(color == "negro" and x == 7):
			return True

		else:
			return False


	def convertirEnDama(tablero,x,y,color):
		#para blanco
		if(color == "blanco" and tablero[x][y] == 1):
			tablero[x][y] = 2
		#para negro
		elif(color == "negro" and tablero[x][y] == 3):
			tablero[x][y] = 4

		return tablero

	def contarFichas (tablero, color):
		cont = 0
		if(color == "blanco"):
			for i in range(len(tablero)):
				for j in range(len(tablero[i])):
					if(tablero[i][j] == 1):
						cont += 1
					elif(tablero[i][j] == 2):
						cont += 3
		if(color == "negro"):
			for i in range(len(tablero)):
				for j in range(len(tablero[i])):
					if(tablero[i][j] == 3):
						cont +=1
					elif(tablero[i][j] == 4):
						cont +=3
		return cont

	def finJuego (tablero):
		if(Tablero.contarFichas(tablero,"blanco")==0 or Tablero.contarFichas(tablero,"negro")==0):
			return True
		elif(len(Tablero.generarMovimientos(tablero,"blanco"))==0 or len(Tablero.generarMovimientos(tablero,"negro"))==0):
			return True
		return False

#--------------------------------Funciónes para realizar el minimax(backtraking)--------------------------------
	def generarMovimientos(tablero,jugador):
		tableroActual = tablero.copy()
		comer=False
		captura = []
		mover = []
		x=0
		y=0
		if(jugador == "blanco"):
			while(x<len(tableroActual)):
				while(y<len(tableroActual[x])):
					if(tableroActual[x][y] == 1):
						if(movimiento.validarComerDe(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDe(tableroActual,jugador,x,y))
						if(movimiento.validarComerIz(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerIz(tableroActual,jugador,x,y))
						if(comer == False):
							if(movimiento.validarMovDe(tableroActual,jugador,x,y)):
								mover.append(movimiento.moverDe(tableroActual,jugador,x,y))
							if(movimiento.validarMovIz(tableroActual,jugador,x,y)):
								mover.append(movimiento.moverIz(tableroActual,jugador,x,y))
					elif(tableroActual[x][y] == 2):
						if(movimiento.validarComerDamaDeU(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaDeU(tableroActual,jugador,x,y))
						if(movimiento.validarComerDamaDeD(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaDeD(tableroActual,jugador,x,y))
						if(movimiento.validarComerDamaIzD(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaIzD(tableroActual,jugador,x,y))
						if(movimiento.validarComerDamaIzU(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaIzU(tableroActual,jugador,x,y))
						if(comer == False):
							i=0
							while(movimiento.validarMovIz(tableroActual,jugador,x-i,y-i)):
								mover.append(movimiento.moverIz(tableroActual,jugador,x-i,y-i))
								i+=1
							i=0
							while(movimiento.validarMovIzInv(tableroActual,jugador,x+i,y-i)):
								mover.append(movimiento.moverIzInv(tableroActual,jugador,x+i,y-i))
								i+=1
							i=0
							while(movimiento.validarMovDe(tableroActual,jugador,x-i,y+i)):
								mover.append(movimiento.moverDe(tableroActual,jugador,x+i,y+i))
								i+=1
							i=0
							while(movimiento.validarMovDeInv(tableroActual,jugador,x+i,y+i)):
								mover.append(movimiento.moverDeInv(tableroActual,jugador,x+i,y+i))
								i+=1
					y+=1
				y=0
				x+=1
		if(jugador == "negro"):
			while(x<len(tableroActual)):
				while(y<len(tableroActual[x])):
					if(tableroActual[x][y] == 3):
						if(movimiento.validarComerDe(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDe(tableroActual,jugador,x,y))
						if(movimiento.validarComerIz(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerIz(tableroActual,jugador,x,y))
						if(comer == False):
							if(movimiento.validarMovDe(tableroActual,jugador,x,y)):
								mover.append(movimiento.moverDe(tableroActual,jugador,x,y))
							if(movimiento.validarMovIz(tableroActual,jugador,x,y)):
								mover.append(movimiento.moverIz(tableroActual,jugador,x,y))
					elif(tableroActual[x][y] == 4):
						if(movimiento.validarComerDamaDeU(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaDeU(tableroActual,jugador,x,y))
						if(movimiento.validarComerDamaDeD(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaDeD(tableroActual,jugador,x,y))
						if(movimiento.validarComerDamaIzD(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaIzD(tableroActual,jugador,x,y))
						if(movimiento.validarComerDamaIzU(tableroActual,jugador,x,y)):
							comer = True
							captura.append(movimiento.comerDamaIzU(tableroActual,jugador,x,y))
						if(comer == False):
							i=0
							while(movimiento.validarMovIz(tableroActual,jugador,x+i,y-i)):
								mover.append(movimiento.moverIz(tableroActual,jugador,x+i,y-i))
								i+=1
							i=0
							while(movimiento.validarMovIzInv(tableroActual,jugador,x-i,y-i)):
								mover.append(movimiento.moverIzInv(tableroActual,jugador,x-i,y-i))
								i+=1
							i=0
							while(movimiento.validarMovDe(tableroActual,jugador,x+i,y+i)):
								mover.append(movimiento.moverDe(tableroActual,jugador,x+i,y+i))
								i+=1
							i=0
							while(movimiento.validarMovDeInv(tableroActual,jugador,x-i,y+i)):
								mover.append(movimiento.moverDeInv(tableroActual,jugador,x-i,y+i))
								i+=1
					y+=1
				y=0
				x+=1
		if(comer == True):
			return captura
		else:
			return mover




	def vueltaAtras(tablero,mejorTablero,profundidad,nivel,jugador,valor):
		tableroActual = tablero.copy()
		oponente = Tablero.invertirColor(jugador)

		if(nivel == profundidad or Tablero.finJuego(tableroActual)):
			if(profundidad %2 !=0):
				if(Tablero.minimax(tableroActual,jugador)<valor[0]):
					valor[0] = Tablero.minimax(tableroActual,jugador)
					return True
			else:
				if(Tablero.minimax(tableroActual,jugador)>valor[0]):
					valor[0] = Tablero.minimax(tableroActual,jugador)
					return True
			return False
		else:
			tablerosPosibles = Tablero.generarMovimientos(tableroActual,jugador)
			for x in range(0,len(tablerosPosibles)):
				candidato = tablerosPosibles[x].copy()
				if(Tablero.vueltaAtras(candidato,mejorTablero,profundidad,nivel+1,oponente,valor)):
					if(nivel == 0):
						mejorTablero[0] = candidato
					else:
						return True


def main():
	
	tab = Tablero.generarTablero()
	tab2 = [tab]
	valor = []
	valor.append(0)
	#print(Tablero.generarMovimientos(tab,"negro"))
	Tablero.vueltaAtras(tab,tab2,3,0,"blanco",valor)

	print(tab2[0])
main()