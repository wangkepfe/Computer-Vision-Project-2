import numpy as np
import cv2

targetSize = (1000,1000)
img2 = cv2.imread('./IMG2.JPG')
img3 = cv2.imread('./IMG3.JPG')
img4 = cv2.imread('./IMG4.JPG')
img5 = cv2.imread('./IMG5.JPG')

H12 = np.float32([[0,0,0],[0,0,0],[0,0,0]])
H13 = np.float32([[0,0,0],[0,0,0],[0,0,0]])
H14 = np.float32([[0,0,0],[0,0,0],[0,0,0]])
H15 = np.float32([[0,0,0],[0,0,0],[0,0,0]])

im_dst2 = cv2.warpPerspective(img2, H12, targetSize)
im_dst3 = cv2.warpPerspective(img3, H13, targetSize)
im_dst4 = cv2.warpPerspective(img4, H14, targetSize)
im_dst5 = cv2.warpPerspective(img5, H15, targetSize)
