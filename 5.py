import cv2
import math
import numpy as np

# downscale and read image
imagem1=cv2.imread('52.png')
#s_img = cv2.imread("smaller_image.png")
imagem = cv2.imread("background.png")
x_offset=y_offset=300
imagem[y_offset:y_offset+imagem1.shape[0], x_offset:x_offset+imagem1.shape[1]] = imagem1
imagem = cv2.bitwise_not(imagem)
#cv2.imshow("contours", imagem)
img = cv2.pyrDown(imagem)
# threshold image
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                  127, 255, cv2.THRESH_BINARY)
# get contours from image
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

# for each contour
#print contours
for i in range (0,len(contours)):
    print cv2.contourArea(contours[i])

sum=0
for cnt in contours:
    # get convex hull
    hull = cv2.convexHull(cnt)
    #print [hull]
    #print cv2.contourArea([hull])
    for i in range(0, len([hull])):
        print cv2.contourArea([hull][i])
        sum+=cv2.contourArea([hull][i])
    # draw it in red color
    cv2.drawContours(img, [hull], -1, (225, 225, 0), 1)
print sum,"##"
cv2.imshow("contours", cv2.bitwise_not(img))

ESC = 27
'''while True:
    keycode = cv2.waitKey(25)
    if keycode != -1:
        keycode = 0xFF
        if keycode == ESC:
            break

cv2.destroyAllWindows()'''
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()