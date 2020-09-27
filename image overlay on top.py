# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:37:05 2020

@author: akash
"""

from PIL import Image
import cv2
import numpy as np

zoom = 0.1
steelSize = (842, 595)
pastePos= (150,150)


img = Image.open("spot.png")
img = img.resize((int(img.size[0]*zoom), int(img.size[1]*zoom)),Image.ANTIALIAS)
background = Image.open("metal.jpg")
background = background.resize(steelSize,Image.ANTIALIAS)
background.paste(img, pastePos, img)
#background.save('how_to_superimpose_two_images_02.png',"PNG")
#background.show()

background = np.array(background)
cv2.imshow('combined', background)
