# Based on: https://cvexplained.wordpress.com/2020/06/13/image-transition-fade-in-fade-out/
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
 
img1 = cv2.imread('./src/fondo_1.png',1)
img2= cv2.imread('./src/fondo_2.jpg',1)
 
first_image = cv2.resize(img1, (0,0), fx=0.4, fy=0.4)
second_image = cv2.resize(img2, (0,0), fx=0.4, fy=0.4)
# second_image = cv2.resize(img2, (672, 420))
 
img1_weight = 0
reverse = False # this is used to reverse the weight
 
while 1:
     
    # continue to add or decrease weight 
    if reverse:
        img1_weight -= 0.1
    else:
        img1_weight += 0.1
         
    # if img1_weight goes up, then img2_weight goes down accordingly and vice versa.
    img2_weight = 1 - img1_weight  
     
    dst = cv2.addWeighted(first_image, img1_weight , second_image, img2_weight , 0)
     
    # we will have a 0.15 transition between frames for a smooth transition
    time.sleep(0.15)    
 
    cv2.imshow('dst',dst)
     
    # if threshold is reached set reverse to True
    if img1_weight > 1: 
         
       # lets have 1 second wait before reversing
       time.sleep(1)     
       reverse =True
         
    # if  inverse threshold is reached set reverse to False
    elif img1_weight < 0:          
        time.sleep(1)
        reverse =False
    
    if cv2.waitKey(1)  & 0xFF == ord('q'):  
          break
              
cv2.destroyAllWindows()