import cv2
import numpy as np
img = cv2.imread('gapclosed_image.tiff', -1)
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imBw = cv2.threshold(imGray, 250, 255, cv2.THRESH_BINARY)

invBwMesh = cv2.bitwise_not(imBw)
Mask = np.ones(imBw.shape, dtype="uint8") * 255

connectivity = 8

kernel = np.ones((5,5),np.uint8)
dilation = cv2.erode(imBw,kernel,iterations = 3)
output = cv2.connectedComponentsWithStats(dilation, connectivity, cv2.CV_32S)
num_labels = output[0]
labels = output[1]
stats = output[2]
centroids = output[3]


print (num_labels)

for i in range(0,num_labels):
   
    print labels[i]
  


#print (centroids)

cv2.imshow('original',img)
cv2.imshow('image',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()


