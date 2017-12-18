import cv2 
import numpy as np

#loads an image in greyscale mode
img = cv2.imread('lena.png', 0)
img1 = cv2.imread('lena_closed.png', 0)
kernel = np.ones((5,5),np.uint8)
#img = cv2.dilate(img,kernel,iterations = 1)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("lena_closed_cv2.png",img)
#cv2.imwrite('lenaopening.png',img) 
def display(img):
    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    cv2.imshow('erosion',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


difference = cv2.subtract(img,img1)
result = not np.any(difference) #if diff is zero will return false

if result is True:
    print ("same")
else:
    cv2.imwrite("result.jpg", difference)
    print("diff")