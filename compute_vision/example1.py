import numpy as np
import cv2 as cv

def get_points(img, calib):
    rows=7
    columns=7
    #convertimos a escala de grises para facilitar la deteccion de las esquinas
    gray = cv.cvtColor(img,
                       cv.COLOR_BGR2GRAY)
    # Buscamos las esquinas del tablero
    ret, corners = cv.findChessboardCorners(gray,
                                            (rows, columns),
                                            None)

    # Comprobamos si ha encontrado un tablero, en cuyo caso continiamos. Si no, devolvemos solo la imagen
    if ret == True:
        #Calcula la diferencia entre los puntos detectados de los elementos para dibujar los cuadrados más adelante
        x1,y1,w,h=cv.boundingRect(corners[0])
        x2,y2,w,h=cv.boundingRect(corners[8])
        if(x1<x2):
            witdth=x2-x1
        else:
            witdth=x1-x2
        if(y1<y2):
            high=y2-y1
        else:
            high=y1-y2

        #Extraemos las coordenadas x y de los puntos y los almacenamos en un array
        corn=[]
        for c in corners:
            x,y,w,h=cv.boundingRect(c)
            corn.append([[x,y]])

        #Calculamos las coordenadas para los puntos restantes
            #Primero calculamos los de la parte de la izquierda al grupo detectado
        for i in range(7):
            x3=int(corn[7*i+i][0][0]) - witdth
            y3=int(corn[7*i+i][0][1])
            corn.insert(i*7+i,[[x3,y3]])

            #Ahora a por los de la derecha
        for i in range(7):
            x3=int(corn[7*(i+1)+2*i][0][0]) + witdth
            y3=int(corn[7*(i+1)+2*i][0][1])
            corn.insert(7*(i+1)+2*i+1,[[x3,y3]])

            #Ahora a por los de arriba
        for i in range(9):
            x3=int(corn[i*2][0][0])
            y3=int(corn[i*2][0][1])-high
            corn.insert(i,[[x3,y3]])

            # Ahora a por los de abajo
        for i in range(9):
            x3 = int(corn[9 * 7 + i][0][0])
            y3 = int(corn[9 * 7 + i][0][1]) + high
            corn.insert(9 * 8 + i, [[x3, y3]])


        #Dibuja encima rectangulos o devuelve el array
        if(calib):
            for r in range(8):
                for c in range(8):
                    x = int(corn[9*r+c][0][0])
                    y = int(corn[9*r+c][0][1])
                    cv.rectangle(img,
                                 (x, y),
                                 (x + witdth, y + high),
                                 (36, 255, 12),
                                 2)
            return True,img;
        else:
            return True, corn;
    return False,img;

def resizeimg(original, scale_percent):
    #first parameter is the image, and the second the porcentage to resize the image
    print('Original Dimensions : ', original.shape)
    width = int(original.shape[1] * scale_percent / 100)
    height = int(original.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv.resize(original, dim, interpolation=cv.INTER_AREA)
    return img

def showimage(img,waits):
    #show image and depends of the value of "waits", wait a key or not
    cv.imshow("imagen",img)
    if waits:
        cv.waitKey(0)

def detect_checkertype(imageFrame):
    checkertype=0
    hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
    # Set range for red color and
    # define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv.inRange(hsvFrame, red_lower, red_upper)

    # Set range for green color and
    # define mask
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv.inRange(hsvFrame, green_lower, green_upper)

    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv.inRange(hsvFrame, blue_lower, blue_upper)
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv.dilate(red_mask, kernal)
    res_red = cv.bitwise_and(imageFrame, imageFrame,
                              mask=red_mask)

    # For green color
    green_mask = cv.dilate(green_mask, kernal)
    res_green = cv.bitwise_and(imageFrame, imageFrame,
                                mask=green_mask)

    # For blue color
    blue_mask = cv.dilate(blue_mask, kernal)
    res_blue = cv.bitwise_and(imageFrame, imageFrame,
                               mask=blue_mask)

    # Creating contour to track red color
    _, contours, hierarchy = cv.findContours(red_mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            checkertype=1
            x, y, w, h = cv.boundingRect(contour)
            imageFrame = cv.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv.putText(imageFrame, "Red Colour", (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

            # Creating contour to track green color
    _, contours, hierarchy = cv.findContours(green_mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            checkertype=2
            x, y, w, h = cv.boundingRect(contour)
            imageFrame = cv.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)

            cv.putText(imageFrame, "Green Colour", (x, y),
                        cv.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

            # Creating contour to track blue color
    _, contours, hierarchy = cv.findContours(blue_mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            checkertype=3
            x, y, w, h = cv.boundingRect(contour)
            imageFrame = cv.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)

            cv.putText(imageFrame, "Blue Colour", (x, y),
                        cv.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
    showimage(imageFrame, True)
    return checkertype

def checker_detection(arrays,img):
    checkboard = np.zeros((8, 8))
    print(checkboard, checkboard.shape)
    #Vamos a dividir la imagen en casillas
        #para ello primero sacamos el tamaño de los lados
    x1=arrays[0][0][0]
    y1=arrays[0][0][1]
    x2 = arrays[10][0][0]
    y2 = arrays[10][0][1]
    if (x1 < x2):
        witdth = x2 - x1
    else:
        witdth = x1 - x2
    if (y1 < y2):
        high = y2 - y1
    else:
        high = y1 - y2
    #Ahora vamos tomando los cuadrados de la imagen de 1 en 1
    for r in range(8):
        for c in range(8):
            x = int(arrays[9 * r + c][0][0])
            y = int(arrays[9 * r + c][0][1])
            crop_img = img[y:y + high, x:x + witdth]
            showimage(crop_img,True)
            checkboard[r][c]=detect_checkertype(crop_img)
    print(checkboard, checkboard.shape)
    return True, checkboard;


def opencv_management(option):
    #Esta funcion devuelve un booleano referenciando a si ha detectado el tablero, y otro valor(imagen o array)
    #dependiendo de la opcion seleccionada
    #Esta funcion tiene las siguientes opciones
        # 1 -Detecta el tablero en tiempo real y la representa sobre el tablero hasta que se pulsa una tecla(se usa para calibrar)
        # 2 -Devuelve un array con las posiciones de las esquinas (tablero una vez calibrado)
        # 3 -Devuelve un array con la disposicion de las fichas en el tablero
    #en cualquier caso tomaremos la imagen de la webcam
    cap = cv.VideoCapture(0)
    if(option==1):
        print("PRESIONA q para salir de esta vista")
        while (True):
            ret, frame = cap.read()
            detected,image = get_points(frame, True)
            showimage(image, False)
            if cv.waitKey(1) & 0xFF == ord('q'):
                if (detected): print("Tablero detectado")
                break
        cap.release()
        cv.destroyAllWindows()

    elif(option==2):
        ret, frame = cap.read()
        detected, arrays = get_points(frame, False)
        if(detected): print("Tablero detectado")
        return detected, arrays;

    elif(option==3):
        ret, frame = cap.read()
        detected, arrays = get_points(frame, False)

        if (detected):
            print("Tablero detectado")
            errors, arrays = checker_detection(arrays,frame)
        return False,  arrays;
    else:
        print("tienes que elegir una opcion valida")


def main():
    opencv_management(3)


main()
