import cv2
import numpy as np

from PIL import Image

'''tmp = Image.open('img2.png')
qwe = cv2.imread("img2.png")
iw, ih = qwe.shape[0], qwe.shape[1]
size = int(iw *1.04), int(ih *1.04)
tmp = tmp.resize(size)
tmp.show("a")
tmp.save("ask.png")
image = np.zeros((tmp.size[1], tmp.size[0], 3), np.uint8)
image=cv2.bitwise_not(image)
cv2.imwrite("image.png",image)
x=cv2.imread("image.png")
y=cv2.imread("img2.png")
print x.shape, y.shape
x[int((x.shape[0]-y.shape[0])/2):int((x.shape[0]-y.shape[0])/2)+ y.shape[0], int((x.shape[1]-y.shape[1])/2):int((x.shape[1]-y.shape[1])/2)+y.shape[1]] = y
cv2.imwrite("ask1.png",x)
img = Image.open('ask1.png')
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in xrange(height):
    for x in xrange(width):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)
background = img
foreground = Image.open("ask.png")

Image.alpha_composite(background, foreground).save("test3.png")'''



'''x=cv2.imread("xyz.png")
y=cv2.imread("img2.png")
x[0: y.shape[0], 0:y.shape[1]] = y
cv2.imwrite("ask.png",x)'''

'''layer1 = Image.open("ask.png")
layer2 = Image.open("img4.png")
final1 = Image.new("RGBA", layer1.size)
final1.paste(layer1, (0,0), layer1)
final1.paste(layer2, (0,0), layer2)
final2 = Image.new("RGBA", layer1.size)
final2 = Image.alpha_composite(final2, layer1)
final2 = Image.alpha_composite(final2, layer2)
final2.show("a")
final2.save("bor.png","PNG")'''

im2=cv2.imread("img2.png")
im2[np.where((im2 == [0,0,0]).all(axis = 2))] = [0,255,0]
cv2.imshow("a",im2)
cv2.waitKey()