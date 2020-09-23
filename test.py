import cv2
import numpy as np
import os
import random
from scipy.ndimage import maximum_filter, minimum_filter


def viewImage(image, name_of_window):                       # Вывод изображения на экран
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def sp_noise(image,prob):                                   # Наложение шума соль/перец

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('dodge.jpg')
noise_img = sp_noise(image,0.05)                            # 
cv2.imwrite('sp_noise.jpg', noise_img)

edited = cv2.imread("sp_noise.jpg")
viewImage(edited, "Nosied")

kernel = np.ones((5,5),np.float32)/25                       # Усреднение
dst = cv2.filter2D(edited,-1,kernel)
viewImage(dst,"Usrednenie")

blur = cv2.bilateralFilter(edited,9,75,75)                  # Билатериальный фильтр.
viewImage(blur,"Bilaterialniy")

median = cv2.medianBlur(edited,5)                           # Медианный фильтр
viewImage(median,"Median")

