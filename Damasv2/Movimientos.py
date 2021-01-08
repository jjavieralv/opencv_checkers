import array

#Las funciones validar comer comprueban si la pieza tiene opción a comer 

	#Peones
def validarComerDe(tablero,color,x,y):
	if color == "blanco":
		if tablero[x+1][y+1] == 3 or tablero[x+1][y+1] == 4:
			if tablero[x+2][y+2] == 0:
				return True
	else: 
		if tablero[x-1][y+1] == 1 or tablero[x-1][y+1] == 2:
			if tablero[x-2][y+2] == 0:
				return True
	return False

def validarComerDeInv(tablero,color,x,y):
	if color == "blanco":
		if tablero[x-1][y+1] == 3 or tablero[x-1][y+1] == 4:
			if tablero[x-2][y+2] == 0:
				return True
	else: 
		if tablero[x+1][y+1] == 1 or tablero[x+1][y+1] == 2:
			if tablero[x+2][y+2] == 0:
				return True
	return False

def validarComerIz(tablero,color,x,y):
	if color == "blanco":
		if tablero[x+1][y-1] == 3 or tablero[x+1][y-1] == 4:
			if tablero[x+2][y-2] == 0:
				return True
	else: 
		if tablero[x-1][y-1] == 1 or tablero[x-1][y-1] == 2:
			if tablero[x-2][y-2] == 0:
				return True
	return False

def validarComerIzInv(tablero,color,x,y):
	if color == "blanco":
		if tablero[x-1][y-1] == 3 or tablero[x-1][y-1] == 4:
			if tablero[x-2][y-2] == 0:
				return True
	else: 
		if tablero[x+1][y-1] == 1 or tablero[x+1][y-1] == 2:
			if tablero[x+2][y-2] == 0:
				return True
	return False

	#Dama
def validarComerDamaDeU(tablero,color,x,y):
	x1=x, y1=y
	if color == "blanco":
		while(y1<8):
			if(validarComerDe(tablero,"blanco",x1,y1)):
				return True
			y1+=1
			x1+=1
		return False
	else:
		while(y1>=0):
			if(validarComerDe(tablero,"negro",x1,y1)):
				return True
			y1+=1
			x1-=1
		return False

def validarComerDamaDeD(tablero,color,x,y):
	x1=x, y1=y
	if color == "blanco":
		while(y1<8):
			if(validarComerDeInv(tablero,"blanco",x1,y1)):
				return True
			y1+=1
			x1-=1
		return False
	else:
		while(y1>=0):
			if(validarComerDeInv(tablero,"negro",x1,y1)):
				return True
			y1+=1
			x1+=1
		return False

def validarComerDamaIzU(tablero,color,x,y):
	x1=x, y1=y
	if color == "blanco":
		while(y1>=0):
			if(validarComerIz(tablero,"blanco",x1,y1)):
				return True
				break
			y1-=1
			x1+=1
		return False
	else:
		while(y1>=0):
			if(validarComerIz(tablero,"negro",x1,y1)):
				return True
				break
			y1-=1
			x1-=1
		return False

def validarComerDamaIzD(tablero,color,x,y):
	x1=x, y1=y
	if color == "blanco":
		while(y1>=0):
			if(validarComerIzInv(tablero,"blanco",x1,y1)):
				return True
				break
			y1-=1
			x1-=1
		return False
	else:
		while(y1>=0):
			if(validarComerIzInv(tablero,"negro",x1,y1)):
				return True
				break
			y1-=1
			x1+=1
		return False
	

		 		
#Validar movimiento

def validarMovDe(tablero,color,x,y):
	if color == "blanco":
		if tablero[x+1][y+1] == 0:
			return True
	else: 
		if tablero[x-1][y+1] == 0:
			return True
	return False

def validarMovDeInv(tablero,color,x,y):
	if color == "blanco":
		if tablero[x-1][y+1] == 0:
			return True
	else: 
		if tablero[x+1][y+1] == 0:
			return True
	return False

def validarMovIz(tablero,color,x,y):
	if color == "blanco":
		if tablero[x+1][y-1] == 0:
			return True
	else: 
		if tablero[x-1][y-1] == 0:
			return True
	return False

def validarMovIzInv(tablero,color,x,y):
	if color == "blanco":
		if tablero[x-1][y-1] == 0:
			return True
	else: 
		if tablero[x+1][y-1] == 0:
			return True
	return False

