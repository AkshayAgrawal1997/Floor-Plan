import cv2
import numpy as np
img1 = cv2.imread('file_0.jpg')
#print (img.shape)
#print (img2.shape)
'''cv2.imshow('x',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)img2 = cv2.imread('door1.png')

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst'''
'''x_offset=y_offset=50
img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]] = img2
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

r = 80.0 / img2.shape[1]
dim = (80, int(img2.shape[0] * r))

# perform the actual resizing of the image and show it
resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
#kernel = np.ones((5,5),np.uint8)
#resized=cv2.morphologyEx(resized, cv2.MORPH_GRADIENT, kernel)
x_offset=360
y_offset=146
(h, w) = resized.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
resized = cv2.warpAffine(resized, M, (w, h))
cv2.imshow('r',resized)
#x,y,w,h = cv2.boundingRect(resized)
#cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),2)
#img1[y_offset:y_offset+resized.shape[0], x_offset:x_offset+resized.shape[1]] = resized
#cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()