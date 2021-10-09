import cv2
import numpy as np
import random


piros = [(2, 10, 124),"piros"]
kek = [(186, 72, 0), "kék"]
zold = [(87, 122, 59), "zöld"]
cian = [(238, 238, 175), "cián"]
szurke = [(85, 85, 85), "szürke"]
sarga = [(53, 225, 255),"sárga"]
pink = [(138, 33, 224),"pink"]
lila = [(255, 0, 191), "lila"]
narancs = [(0, 103, 255), "narancs"]
magenta = [(139, 0, 139), "magenta"]
brown = [(0, 75, 150),"barna"]
turkiz = [(208, 224, 64), "türkizkék"]
mandula = [(205, 222, 239),"mandula"]
arany = [(0, 215,255),"arany"]
bordo = [(52, 23, 127), "bordo"]
DARKKHAKI = [(107, 183, 189),"darkkhaki"]
INDIGO = [(205, 90, 106),"Indigo"]
OLIVE = [(0, 128, 128),"Oliva"]
DARKSLATEGRAY = [(79, 79, 47),"darkslategray"]
PERU = [(63, 133, 205),"Peru"]



colors= [piros[0], kek[0], zold[0], cian[0], szurke[0], sarga[0], pink[0], lila[0], narancs[0], magenta[0], brown[0], turkiz[0], mandula[0], arany[0], bordo[0],DARKKHAKI[0],INDIGO[0],OLIVE[0],DARKSLATEGRAY[0],PERU[0]]
colors_full = [piros, kek, zold, cian, szurke, sarga, pink, lila, narancs, magenta, brown, turkiz, mandula, arany, bordo,DARKKHAKI,INDIGO,OLIVE,DARKSLATEGRAY,PERU]

img = cv2.imread("shapes.png");
#img = cv2.imread("painted.png");
#img = cv2.imread("painted2.png");
#img = cv2.imread("painted3.png");
#img = cv2.imread("painted4.png");
#img = cv2.imread("painted5.png");
cv2.imshow("Eredeti",img)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

noise = np.zeros(gray.shape, np.int16)
cv2.randn(noise, 0.0, 20.0)

imnoise2 = cv2.add(gray, noise, dtype=cv2.CV_16SC1)
imnoisenorm = cv2.normalize(imnoise2, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
cv2.imshow('Zajos', imnoisenorm)

filtered = cv2.bilateralFilter(imnoisenorm, 9, 110, 110, cv2.BORDER_DEFAULT);
canny = cv2.Canny(filtered, 120, 255, 1)


cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]




for n, cnt in enumerate(cnts):
    approx = cv2.approxPolyDP(
        cnt, 0.02 * cv2.arcLength(cnt, True), True)
    print("A következő színek egy objektumot vesznek körbe:")

    n = approx.ravel()
    i = 0
    for j in n:
        if (i % 2 == 0):
            x = n[i]
            y = n[i + 1]
            cornered = cv2.circle(img, (x, y), 11, random.choice(colors), -1)
            points = [x, y]
            bgr_s = img[y, x]
            for sk in range(len(colors_full)):
                if np.array_equal(bgr_s, colors_full[sk][0]):
                    print(colors_full[sk][1])

        i = i + 1

cv2.imshow("Sarkok",cornered)
cv2.waitKey(0)
cv2.destroyAllWindows()
