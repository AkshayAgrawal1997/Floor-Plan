import cv2
import math
from PIL import Image

wrap=[[0 for i in range(2)] for j in range(9)]
roll= [0 for i in range(9)]
polar= [[0 for i in range(2)] for j in range(9)]
shape= [[0 for i in range(2)] for j in range(9)]
wrap[0][0]=82.0
wrap[0][1]=80.0
wrap[1][0]=84.0
wrap[1][1]=80.0
wrap[2][0]=84.0
wrap[2][1]=84.0
wrap[3][0]=100.0
wrap[3][1]=112.0
wrap[4][0]=120.0
wrap[4][1]=116.0
wrap[5][0]=120.0
wrap[5][1]=120.0
wrap[6][0]=84.0
wrap[6][1]=84.0


roll[0]=0.0
roll[1]=180.0
roll[2]=270.0
roll[3]=90.0
roll[4]=90.0
roll[5]=90.0
roll[6]=45.0

polar[0][0]=1.0
polar[0][1]=0.25
polar[1][0]=1.0
polar[1][1]=0.75
polar[2][0]=1.0
polar[2][1]=0.5
polar[3][0]=1.0
polar[3][1]=0.5
polar[4][0]=1.0
polar[4][1]=0.5
polar[5][0]=1.0
polar[5][1]=0.5
polar[6][0]=1.0
polar[6][1]=0.25

shape[0][0]=400.083033
shape[0][1]=218.02467
shape[1][0]=720.522564
shape[1][1]=252.401324
shape[2][0]=778.226234
shape[2][1]=355.531288
shape[3][0]=71.04934
shape[3][1]=159.093262
shape[4][0]=71.04934
shape[4][1]=324.837847
shape[5][0]=71.04934
shape[5][1]=463.572202
shape[6][0]=309.0
shape[6][1]=578.0

for i in range(0,7):
    if(i==0 or i==1 or i==2):
        img = Image.open('img2.png')
    elif(i==3 or i==4 or i==5):
        img = Image.open('img3.png')
    else:
        img = Image.open('img4.png')
    col = wrap[i][0]
    row = wrap[i][1]
    shapex = shape[i][0]
    shapey = shape[i][1]
    s = img.size
    r = row * 1.0 / s[1]
    dim = row, int(s[0] * r)
    # resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    img.thumbnail(dim, Image.ANTIALIAS)
    resized = img
    '''def rotate_image(mat, angle):
        height, width = mat.shape[:2]
        image_center = (width / 2, height / 2)

        rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)

        radians = math.radians(angle)
        sin = math.sin(radians)
        cos = math.cos(radians)
        bound_w = int((height * abs(sin)) + (width * abs(cos)))
        bound_h = int((height * abs(cos)) + (width * abs(sin)))

        rotation_mat[0, 2] += ((bound_w / 2) - image_center[0])
        rotation_mat[1, 2] += ((bound_h / 2) - image_center[1])

        rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
        return rotated_mat

    img2=rotate_image(resized,0)'''
    # cv2.imwrite("x.png",resized)
    # img2=Image.open('x.png')
    resized = resized.rotate(roll[i], expand=True)
    resized.save("y.png")
    # resized.show()
    # cv2.imshow('a',img2)
    # cv2.imwrite("x.png",img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img2 = cv2.imread('y.png')
    dx = img2.shape[1]
    dy = img2.shape[0]
    r = 1.0
    thetha = polar[i][1] * 2 * 3.141592653589793
    finalthetha = 0.0
    finalr = 0.0
    d1 = 0.0
    d2 = 0.7853981633974483
    d3 = 1.5707963267948966
    d4 = 2.356194490192345
    d5 = 3.141592653589793
    d6 = thetha % 3.141592653589793
    d7 = 0.0


    def sheary(y):
        return math.atan(math.tan(y) * (dy / 2.0) / (dx / 2.0))


    def shearx(x):
        return math.atan(math.tan(x) * (dx / 2.0) / (dy / 2.0))


    if (d6 >= d1 and d6 < d2):
        # d7=math.atan(math.tan(d6)*(dy/2.0)/(dx/2.0))
        d7 = sheary(d6)
    elif (d6 >= d2 and d6 < d3):
        d7 = d3 - shearx(d3 - d6)
    elif (d6 >= d3 and d6 < d4):
        d7 = d3 + shearx(d6 - d3)
    elif (d6 >= d4 and d6 < d5):
        d7 = d5 - sheary(d5 - d6)
    if (thetha < 3.141592653589793):
        finalthetha = d7
    else:
        finalthetha = 3.141592653589793 + d7

    print finalthetha, "\n"

    temp = thetha % 3.141592653589793
    d = math.atan(dy / dx)
    if (temp >= 0.0 and temp < d):
        finalr = dx / 2.0 / math.cos(temp)
    elif (temp >= d and temp < d3):
        finalr = dy / 2.0 / math.cos(d3 - temp)
    elif (temp >= d3 and temp < d5 - d):
        finalr = dy / 2.0 / math.cos(temp - d3)
    else:
        finalr = dx / 2.0 / math.cos(d5 - temp)

    print finalr, "\n"
    print math.cos(finalthetha)
    print finalr * math.cos(finalthetha), " ", finalr * math.sin(finalthetha)

    newdx = finalr * math.cos(finalthetha)
    newdy = finalr * math.sin(finalthetha)
    if (finalthetha <= d5):
        shapex = shapex - (dx / 2 + newdx)
        shapey = shapey - (dy / 2 + newdy)
    else:
        shapex = shapex - (dx / 2 + newdx)
        shapey = shapey - (dy / 2 + newdy)

    print shapex, shapey

    floor = cv2.imread('groundfilled-01 - Copy.png')
    r1 = 1882
    r = r1 * 1.0 / floor.shape[1]
    dim = r1, int(floor.shape[0] * r)
    cv2.resize(floor, dim, interpolation=cv2.INTER_AREA)

    x_offset = int(shapex)
    y_offset = int(shapey)
    print x_offset, y_offset
    # floor[y_offset:y_offset+dy, x_offset:x_offset+dx] = img2
    # cv2.imwrite("t.png",floor)
    # cv2.imshow("x",img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    from PIL import Image, ImageDraw, ImageFont

    img = Image.open('y.png')
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in xrange(height):
        for x in xrange(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    img.save("f.png", "PNG")
    filename = 'f.png'
    ironman = Image.open(filename, 'r')
    filename1 = 'groundfilled-01 - Copy.png'
    bg = Image.open(filename1, 'r')
    bg.thumbnail(dim, Image.ANTIALIAS)
    text_img = Image.new('RGBA', (bg.size[0], bg.size[1]), (0, 0, 0, 0))
    text_img.paste(bg, (0, 0))

    text_img.paste(ironman, (x_offset, y_offset), mask=ironman)
    #text_img.show()
    text_img.save("groundfilled-01 - Copy.png")



