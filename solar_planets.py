import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            3,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (130,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (290, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (380, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (480, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (670, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (930, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1080, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.imshow("output",img)

cv2.waitKey(0)
