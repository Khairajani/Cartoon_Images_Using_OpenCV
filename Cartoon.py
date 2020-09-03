import cv2
import os
import numpy as np

def cartoonify(img_rgb):    

    numBilateralFilters = 15

    img_color = img_rgb
    for _ in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 14, 14, 7)
    
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    img_edge = cv2.adaptiveThreshold(img_blur, 255 ,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 3, 2)
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    return cv2.bitwise_and(img_color, img_edge)

path_of_image = "/home/himanshu/him.jpg"
img = cv2.imread(path_of_image)
img = cv2.resize(img,(600,600))
img_cartoon = cartoonify(img)
stack = np.hstack([img,img_cartoon])
cv2.imshow("Stacked images",stack)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()


    
