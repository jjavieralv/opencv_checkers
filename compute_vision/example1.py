import cv2
import numpy as np
def resizeimg(original, scale_percent):
    #first parameter is the image, and the second the porcentage to resize the image
    print('Original Dimensions : ', original.shape)
    width = int(original.shape[1] * scale_percent / 100)
    height = int(original.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(original, dim, interpolation=cv2.INTER_AREA)
    return img

def showimage(img,waits):
    #show image and depends of the value of "waits", wait a key or not
    cv2.imshow("imagen",img)
    if waits:
        cv2.waitKey(0)

def getconto(img,thresh):
    #this function already works with digital image
    img2=img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_COMPLEX
    cont=0
    for cnt in contours:
        cont+=1
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(img2, [approx], 0, (0,200,0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), font, 1, (0))
        elif len(approx) == 4:
            cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
        elif 6 < len(approx) < 15:
            cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        else:
            cv2.putText(img, "Circle", (x, y), font, 1, (0))
        #cv2.imshow("cpy", img)
        #cv2.waitKey(0)
    return cont

def getconto2(img, thresh):
    cont=0
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_COMPLEX
    for cnt in contours:
        cont+=1
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0, 200, 0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), font, 1, (0))
        elif len(approx) == 4:
            cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
        elif 6 < len(approx) < 15:
            cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        else:
            cv2.putText(img, "Circle", (x, y), font, 1, (0))

        #cv2.imshow("cpy", img)
        #cv2.waitKey(0)
    return cont



def getconto1(img,thresh):
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thrash = cv2.threshold(imgGry, thresh, 255, cv2.THRESH_BINARY)
    # https://stackoverflow.com/questions/55107660/python-cv2-find-contours-minimum-dimensions
    kernel = np.ones((7, 7), np.uint8)
    closing = cv2.morphologyEx(thrash, cv2.MORPH_CLOSE, kernel)
    _th, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conto = 0
    for contour in contours:
        conto += 1
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 200, 0), 1)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

            else:
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        elif len(approx) == 5:
            cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 10:
            cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    showimage(img, True)
    return conto


def main():
    print("Empieza el main")
    orig = cv2.imread('images/checkers.png')
    resized = resizeimg(orig, 300)
    cont=0
    thresh=0
    while (cont!=64 and thresh<255):
        cpy=resized.copy()
        cont=getconto(cpy,thresh)
        print("Con el thresh: ",thresh," ha encontrado cont: ",cont)
        thresh+=10

main()