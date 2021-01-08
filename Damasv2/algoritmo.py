import array
class Tablero:
	def invertirColor(color):
		if (color == "blanco"):
			return "negro"
		else:
			return "blanco"

	def minimax(tablero,color,valor):
		x = contarFichas(tablero,color)
		y = contarFichas(tablero,invertirColor(color))

		return x-y


	def esDama(x,y,color):
		#Se puede llamar directamente a la función convertirEnDama desde aquí
		#para blanca
		if(color == "blanco" and x == 7):
			return True

		#para negra
		elif(color == "negro" and x == 0):
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
			for i in range(8):
				for j in range(8):
					if(tablero[i][j] == 1 or tablero[i][j] == 2):
						cont +=1
		if(color == "negro"):
			for i in range(8):
				for j in range(8):
					if(tablero[i][j] == 3 or tablero[i][j] == 4):
						cont +=1			
					

	def generarMovimientos(tablero, color, profundidad):
		comer = False
		oponente = invertirColor(color)
		jugador = color
		tableroActual = tablero
		tableroFinal = tablero
		numFichas = contarFichas(tablero, color)
		valor = -30
		mejorTablero = []
		fichRevisadas = 0
		x = 0 
		y = 0
		while(fichRevisadas < numFichas and profundidad > 0):
			if(jugador == "blanco"):
				if(tablero[x][y] == 1):
					if(movimiento.validarComerDe(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x+1][y+1] = 0
						tableroActual[x+2][y+2] = 1
						if(esDama(x+2,y+2,jugador)):
							tableroActual = convertirEnDama(tableroActual,x+2,y+2,jugador)
						if(movimiento.validarComerDe(tableroActual,jugador,x+2,y+2) or movimiento.validarComerIz(tableroActual,jugador,x+2,y+2)):
							tableroSig = generarMovimientos(tableroActual,jugador,profundidad-1)
						else:
							tableroSig = generarMovimientos(tableroActual,oponente,profundidad-1)
	    				
						v= minimax(tableroSig,jugador,valor)
						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual
						comer=True
						tableroActual = tablero

					if(movimiento.validarComerIz(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x+1][y-1] = 0
						tableroActual[x+2][y-2] = 1
						if(esDama(x+2,y-2,jugador)):
							tableroActual = convertirEnDama(tableroActual,x+2,y-2,jugador)
						if(movimiento.validarComerDe(tableroActual,jugador,x+2,y-2) or movimiento.validarComerIz(tableroActual,jugador,x+2,y-2)):
							tableroSig = generarMovimientos(tableroActual,jugador,profundidad-1)
						else:
							tableroSig = generarMovimientos(tableroActual,oponente,profundidad-1)
						
						v= minimax(tableroSig,jugador,valor)

						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual

						comer=True
						tableroActual = tablero
						
				if(tablero[x][y] == 1 and comer==False):
					if(movimiento.validarMovDe(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x+1][y+1] = 1
						if(esDama(x+1,y+1,jugador)):
							tableroActual = convertirEnDama(tableroActual,x+1,y+1,jugador)
						tableroSig = generarMovimientos(tableroActual,oponente)
						v= minimax(tableroSig,jugador,valor)

						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual

						tableroActual=tablero
					if(movimiento.validarComerIz(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x+1][y-1] = 1
						if(esDama(x+1,y-1,jugador)):
							tableroActual = convertirEnDama(tableroActual,x+1,y-1,jugador)
						tableroSig = generarMovimientos(tableroActual,oponente)
						
						v= minimax(tableroSig,jugador,valor)
						
						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual

						tableroActual=tablero

			elif(jugador == "negro"):
				if(tablero[x][y] == 3):
					if(movimiento.validarComerDe(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x-1][y+1] = 0
						tableroActual[x-2][y+2] = 3
						if(esDama(x-2,y+2,jugador)):
							tableroActual = convertirEnDama(tableroActual,x-2,y+2,jugador)
						
						if(movimiento.validarComerDe(tableroActual,jugador,x-2,y+2) or movimiento.validarComerIz(tableroActual,jugador,x-2,y+2)):
							tableroSig = generarMovimientos(tableroActual,jugador,profundidad-1)
						else:
							tableroSig = generarMovimientos(tableroActual,oponente,profundidad-1)
						
						v= minimax(tableroSig,jugador,valor)
						
						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual
						comer=True
						tableroActual = tablero

					if(movimiento.validarComerIz(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x-1][y-1] = 0
						tableroActual[x-2][y-2] = 1
						if(esDama(x-2,y-2,jugador)):
							tableroActual = convertirEnDama(tableroActual,x-2,y-2,jugador)
						if(movimiento.validarComerDe(tableroActual,jugador,x-2,y-2) or movimiento.validarComerIz(tableroActual,jugador,x-2,y-2)):
							tableroSig = generarMovimientos(tableroActual,jugador,profundidad-1)
						else:
							tableroSig = generarMovimientos(tableroActual,oponente,profundidad-1)
						
						v= minimax(tableroSig,jugador,valor)

						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual

						comer=True
						tableroActual = tablero
						
				if(tablero[x][y] == 1 and comer==False):
					if(movimiento.validarMovDe(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x-1][y+1] = 1
						if(esDama(x-1,y+1,jugador)):
							tableroActual = convertirEnDama(tableroActual,x-1,y+1,jugador)
						tableroSig = generarMovimientos(tableroActual,oponente)
						v= minimax(tableroSig,jugador,valor)

						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual

						tableroActual=tablero
					if(movimiento.validarComerIz(tableroActual,jugador,x,y)):
						tableroActual[x][y] = 0
						tableroActual[x-1][y-1] = 1
						if(esDama(x-1,y-1,jugador)):
							tableroActual = convertirEnDama(tableroActual,x-1,y-1,jugador)
						tableroSig = generarMovimientos(tableroActual,oponente)
						v= minimax(tableroSig,jugador,valor)
						if(profundidad %2 == 0 and v > valor):
							tableroFinal = tableroActual
						elif(profundidad %2 != 0 and v < valor):
							tableroFinal = tableroActual

						tableroActual=tablero
		return tableroFinal