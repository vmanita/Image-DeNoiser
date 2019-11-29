import numpy as np
import os
from PIL import Image, ImageSequence
import cv2

def process_image(page):
    # process Image
    img = np.asarray(page) 
     # grey
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Apply dilation and erosion to remove some noise       
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)  
    img = cv2.erode(img, kernel, iterations=1)     
    # apply threshold
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    page = Image.fromarray(img)
    return page


