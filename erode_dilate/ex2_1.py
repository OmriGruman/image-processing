# # EX2_1
# build dilate and erode functions
import numpy as np
import matplotlib.pyplot as plt
import cv2

figsize = (10, 10)

img = np.zeros((50, 50))
img[20:30, 20:30] = 1

plt.figure(figsize=figsize)
plt.imshow(img,cmap="gray")
plt.show()

kernel = np.zeros((5,5),dtype=np.uint8)
kernel[2,:] = 1
kernel[:,2] = 1

plt.figure(figsize=figsize)
plt.imshow(kernel,cmap="gray")
plt.show()

def my_dilate(img,kernel):
    #TODO: build dilate function without cv2.dilate
    return (cv2.filter2D(img, -1, kernel) > 0).astype(int)
    

plt.figure(figsize=figsize)
plt.imshow(my_dilate(img,kernel),cmap="gray")
plt.show()

# TODO: show that cv2.dilate and my_dilate are the same using absolute difference
if (my_dilate(img, kernel) == cv2.dilate(img, kernel)).all():
    print("cv2.dilate & my_dilate are the same!")
else: 
    print("try again...")

def my_erode(img,kernel):
    #TODO: build erode function without cv2.erode
    return (cv2.filter2D(img, -1, kernel) == kernel.sum()).astype(int)

plt.figure(figsize=figsize)
plt.imshow(my_erode(img,kernel),cmap="gray")
plt.show()

# TODO: show that cv2.erode and my_erode are the same using absolute difference
if (cv2.erode(img, kernel) == my_erode(img, kernel)).all():
    print("cv2.erode & my_erode are the same!")
else: 
    print("try again...")
