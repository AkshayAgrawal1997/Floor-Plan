'''from PIL import Image
layer1=Image.open("door1.png")
layer2=Image.open("file_91.png")
print layer1.mode
print layer2.mode
#final2 = Image.new("RGBA", layer1.size)
#final2 = Image.alpha_composite(final2, layer1)
#final2 = Image.alpha_composite(final2, layer2)
#x=Image.alpha_composite(layer1,layer2)
x=Image.blend(layer1,layer2, 0.5)
x.show()'''

import os
from PIL import Image, ImageDraw, ImageFont
img = Image.open('bed.png')
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in xrange(height):
    for x in xrange(width):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)

img.save("img5.png", "PNG")
filename='img3.png'
ironman = Image.open(filename, 'r')
filename1='file_91.png'
bg = Image.open(filename1, 'r')
text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
text_img.paste(ironman, (0,0), mask=ironman)
text_img.show()
#text_img.save("ball.png", format="png")