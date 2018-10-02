import numpy as np
import cv2
# Read the image you want connected components of
src = cv2.imread('gapclosed_image.tiff',0)
# Threshold it so it becomes binary
ret, thresh = cv2.threshold(src,214,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# You need to choose 4 or 8 for connectivity type
connectivity = 8
# Perform the operation
output = cv2.connectedComponentsWithStats(src, connectivity, cv2.CV_32S)
# Get the results
# The first cell is the number of labels
num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The third cell is the stat matrix

# The fourth cell is the centroid matrix

for i in range(0,num_labels):
    print labels[i]

print (num_labels)
#cv2.imshow('final', src)
#output = cv2.connectedComponents(src)




