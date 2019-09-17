
import cv2
import numpy

Core = numpy.array(((0, 0.6, 0.1),
                    (0.4, -1.5, 0.1),
                    (0, 0.2, 0)), dtype="float32")

img = cv2.imread('.//picture.jpg')
img = cv2.resize(img, (640, 480))
cv2.imshow('Demo_0', img)

img = cv2.filter2D(img, -1, Core)

cv2.imshow('Demo_1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
