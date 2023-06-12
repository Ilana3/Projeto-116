import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
        "Sol",
        (100,80),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (255, 255, 255))

cv2.putText(img,
        "Mercurio",
        (115,180),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255, 255, 255))

cv2.putText(img,
        "Venus",
        (190,260),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255, 255, 255))

cv2.putText(img,
        "Terra",
        (290,160),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255, 255, 255))

cv2.putText(img,
        "Marte",
        (380,260),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255, 255, 255))

cv2.putText(img,
        "Jupiter",
        (530,50),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (255, 255, 255))

cv2.putText(img,
        "Saturno",
        (750,310),
        cv2.FONT_HERSHEY_COMPLEX,
        0.7,
        (255, 255, 255))

cv2.putText(img,
        "Urano",
        (970,140),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255, 255, 255))

cv2.putText(img,
        "Netuno",
        (1120,285),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (255, 255, 255))

cv2.imshow("resultado",img)
cv2.waitKey(0)