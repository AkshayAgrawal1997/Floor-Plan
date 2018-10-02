#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk
from PIL import ImageTk
APP_TITLE = "Drag & Drop Tk Canvas Images"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200

IMAGE_PATH = ""

def func(imagem):
    #imagem1 = cv2.imread('ab.png')
    # s_img = cv2.imread("smaller_image.png")
    #imagem = cv2.imread("background.png")
    #x_offset = y_offset = 300
    #imagem[y_offset:y_offset + imagem1.shape[0], x_offset:x_offset + imagem1.shape[1]] = imagem1
    imagem = cv2.bitwise_not(imagem)
    # cv2.imshow("contours", imagem)
    img = cv2.pyrDown(imagem)
    # threshold image
    ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                                      127, 255, cv2.THRESH_BINARY)
    # get contours from image
    image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)

    # for each contour
    # print contours
    #for i in range(0, len(contours)):
    #    print cv2.contourArea(contours[i])
    sum=0
    x=0
    for cnt in contours:
        x+=1
        # get convex hull
        hull = cv2.convexHull(cnt)
        #print [hull]
        # print cv2.contourArea([hull])
        for i in range(0, len([hull])):
            sum+= cv2.contourArea([hull][i])
            #print i
        # draw it in red color
        cv2.drawContours(img, [hull], -1, (0, 0, 255), 1)
    #cv2.imshow("contours", img)
    return sum


class CreateCanvasObject(object):
    def __init__(self, canvas, image_name, xpos, ypos, id):
        self.image_id = id
        self.canvas = canvas
        #self.tosave=True
        self.initialx=xpos
        self.initialy=ypos
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos
        self.s_img = cv2.imread(image_name)
        self.tk_image = ImageTk.PhotoImage(
            file="{}{}".format(IMAGE_PATH, image_name))
        self.image_obj = canvas.create_image(
            xpos, ypos, image=self.tk_image)

        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False
        self.mouse_xpos=0
        self.mouse_ypos=0
        self.diffx=0
        self.diffy=0

    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y

            self.canvas.move(self.image_obj,
                             new_xpos - self.mouse_xpos, new_ypos - self.mouse_ypos)

            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
            #print self.mouse_xpos, self.mouse_ypos
        else:
            #self.initialx=event.x
            #self.initialy=event.y
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y
            self.diffx=self.mouse_xpos-self.initialx
            self.diffy=self.mouse_ypos-self.initialy

    def release(self, event):
        self.move_flag = False
        #s_img = cv2.imread("smaller_image.png")
        l_img = cv2.imread("background.png")
        x_offset = event.x-self.diffx-(self.s_img.shape[1]/2)
        y_offset = event.y-self.diffy-(self.s_img.shape[0]/2)
        print x_offset,y_offset
        l_img[y_offset:y_offset + self.s_img.shape[0], x_offset:x_offset + self.s_img.shape[1]] = self.s_img
        #cv2.imshow("a", l_img)
        img1 = cv2.imread('groundfilled-01.png')
        img2 = l_img
        img_bwa = cv2.bitwise_or(img1, img2)
        img_bwa=cv2.cvtColor(img_bwa, cv2.COLOR_BGR2GRAY)
        count= cv2.countNonZero(img_bwa)
        #cv2.imshow("Bitwise AND of Image 1 and 2", img_bwa)

        '''x_img = cv2.imread("img4.png")
        l_img[200-(x_img.shape[0]/2):200 -(x_img.shape[0]/2)+ x_img.shape[0], 500-(x_img.shape[1]/2):500-(x_img.shape[1]/2) + x_img.shape[1]] = x_img
        #cv2.imshow("a",l_img)
        if func(l_img)>21140 or func(l_img)<21100:
            self.canvas.move(self.image_obj,
                             self.initialx-event.x + self.diffx, self.initialy-event.y + self.diffy)
        else:
            self.initialx=event.x-self.diffx
            self.initialy=event.y-self.diffy'''
        #print func(l_img)

        for i in range(1,20):
            if image_i[i]!=0:
                if image_i[i].image_id!=self.image_id:
                    x_img = cv2.imread(image_i[i].image_name)
                    l_img[image_i[i].initialy - (x_img.shape[0] / 2):image_i[i].initialy - (x_img.shape[0] / 2) + x_img.shape[0],image_i[i].initialx - (x_img.shape[1] / 2):image_i[i].initialx - (x_img.shape[1] / 2) + x_img.shape[1]] = x_img
        #cv2.imshow("a",l_img)

        if (func(l_img)>21500 or func(l_img)<21100) or (count!=1494308):
        #if func(l_img)!=2:
            self.canvas.move(self.image_obj,
                             self.initialx-event.x + self.diffx, self.initialy-event.y + self.diffy)
        else:
            self.initialx=event.x-self.diffx
            self.initialy=event.y-self.diffy
        print func(l_img)

image_i=[]
for i in range(20):
    image_i.append(0)

class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)

        self.canvas = tk.Canvas(self, width=1882, height=794, bg='white',
                                highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        #self.image_3 = CreateCanvasObject(self.canvas, "groundfilled-01.png", 941, 397)
        #self.image_1 = CreateCanvasObject(self.canvas, "img2.png", 300, 300)
        #self.image_2 = CreateCanvasObject(self.canvas, "img4.png", 500, 200)
        image_i[0] = CreateCanvasObject(self.canvas, "groundfilled-01.png", 941, 397, 0)
        image_i[1] = CreateCanvasObject(self.canvas, "img2.png", 300, 300, 1)
        image_i[2] = CreateCanvasObject(self.canvas, "img4.png", 500, 200, 2)

    def close(self):
        print("Application-Shutdown")
        self.master.destroy()


def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    # app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))

    app = Application(app_win).pack(fill='both', expand=True)

    app_win.mainloop()


if __name__ == '__main__':
    main()      