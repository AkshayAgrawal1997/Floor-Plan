import Tkinter as tk
from Tkinter import *
import ttk
import imutils
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
#import coverage

from tkFileDialog import askopenfilename
import tkMessageBox
hull_area=0.0
filename = ""
new_filename = ""
groundfilled_img = ""
IMAGE_PATH=""
current_canvas=-1
prev_canvas=-1
img=""
tmp=""
def zoomin():
    if current_canvas>0:
        print current_canvas, "#####"
        global canvas
        global image_i
        canvas.delete(image_i[current_canvas].image_obj)
        #cv2.imshow('a',image_i[current_canvas].s_img)
        qwe = cv2.imread(image_i[current_canvas].image_name)
        iw, ih = qwe.shape[0], qwe.shape[1]
        ################
        ###################################################
        global tmp
        tmp = cv2.imread(image_i[current_canvas].image_name)
        image_i[current_canvas].scale *= 1.1
        size = int(ih * image_i[current_canvas].scale), int(iw * image_i[current_canvas].scale)
        tmp = cv2.resize(tmp, size)
        imagem = cv2.bitwise_not(tmp)
        rotated = imutils.rotate_bound(imagem, image_i[current_canvas].angle)
        tmp = cv2.bitwise_not(rotated)
        cv2.imwrite("temp.png", tmp)
        ##########################################################


        '''global tmp'''
        tmp = Image.open('temp.png')
        # size = int(iw /1.1), int(ih /1.1)
        # tmp = tmp.resize(size)
        tmp = tmp.convert("RGBA")

        pixdata = tmp.load()

        width, height = tmp.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        ######################################
        #image_i[current_canvas].scale *= 1.1
        print size
        img= ImageTk.PhotoImage(tmp)
        image_i[current_canvas].tk_image=img
        # self.img=self.img.subsample(self,x,y=2)
       # print image_i[current_canvas].initialx,image_i[current_canvas].initialy
        #img = ImageTk.PhotoImage(file="C:/Users/Aditya Agrawal/PycharmProjects/untitled2/img2.png")
        image_i[current_canvas].image_obj=canvas.create_image(image_i[current_canvas].initialx,image_i[current_canvas].initialy, image=img)
        #print image_i[current_canvas].initialx, image_i[current_canvas].initialy
        image_i[current_canvas].s_img=cv2.imread("temp.png")
        global hull_area
        hull_area=hull_area-image_i[current_canvas].area
        image_i[current_canvas].area=func(image_i[current_canvas].s_img)
        hull_area+=image_i[current_canvas].area
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button-1>', image_i[current_canvas].focus)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button1-Motion>', image_i[current_canvas].move)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<ButtonRelease-1>', image_i[current_canvas].release)
        image_i[current_canvas].highlight()
        image_i[current_canvas].helper()



def zoomout():
    if current_canvas>0:
        print current_canvas, "#####"
        global canvas
        global image_i
        canvas.delete(image_i[current_canvas].image_obj)
        #cv2.imshow('a',image_i[current_canvas].s_img)
        qwe=cv2.imread(image_i[current_canvas].image_name)
        iw, ih = qwe.shape[0],qwe.shape[1]
        ################
        ###################################################
        global tmp
        tmp=cv2.imread(image_i[current_canvas].image_name)
        image_i[current_canvas].scale/=1.1
        size = int(ih *image_i[current_canvas].scale), int(iw * image_i[current_canvas].scale)
        tmp=cv2.resize(tmp,size)
        imagem = cv2.bitwise_not(tmp)
        rotated = imutils.rotate_bound(imagem, image_i[current_canvas].angle)
        tmp = cv2.bitwise_not(rotated)
        cv2.imwrite("temp.png",tmp)
        ##########################################################


        '''global tmp'''
        tmp = Image.open('temp.png')
        #size = int(iw /1.1), int(ih /1.1)
        #tmp = tmp.resize(size)
        tmp = tmp.convert("RGBA")

        pixdata = tmp.load()

        width, height = tmp.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        ######################################
        print size
        # draw
        #tmp.save("temp.png","PNG", quality=100)
        img= ImageTk.PhotoImage(tmp)
        image_i[current_canvas].tk_image=img
        image_i[current_canvas].image_obj=canvas.create_image(image_i[current_canvas].initialx,image_i[current_canvas].initialy, image=img)
        #print image_i[current_canvas].initialx, image_i[current_canvas].initialy
        image_i[current_canvas].s_img=cv2.imread("temp.png")
        global hull_area
        hull_area = hull_area - image_i[current_canvas].area
        image_i[current_canvas].area = func(image_i[current_canvas].s_img)
        hull_area += image_i[current_canvas].area
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button-1>', image_i[current_canvas].focus)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button1-Motion>', image_i[current_canvas].move)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<ButtonRelease-1>', image_i[current_canvas].release)
        image_i[current_canvas].highlight()
        image_i[current_canvas].helper()

def rotatecw():
    global text
    if current_canvas>0:
        print current_canvas, "#####"
        global canvas
        global image_i
        canvas.delete(image_i[current_canvas].image_obj)
        #iw, ih = image_i[current_canvas].s_img.shape[0],image_i[current_canvas].s_img.shape[1]
        qwe = cv2.imread(image_i[current_canvas].image_name)
        iw, ih = qwe.shape[0], qwe.shape[1]
        global tmp
        tmp = cv2.imread(image_i[current_canvas].image_name)
        size = int(ih*image_i[current_canvas].scale), int(iw*image_i[current_canvas].scale)
        tmp = cv2.resize(tmp, size)
        if text.get("1.0",END)=='':
            image_i[current_canvas]=image_i[current_canvas]
        else:
            image_i[current_canvas].angle+=int(text.get("1.0",END))
        #tmp = cv2.resize(tmp, size)
        imagem = cv2.bitwise_not(tmp)
        rotated = imutils.rotate_bound(imagem, image_i[current_canvas].angle)
        tmp=cv2.bitwise_not(rotated)
        cv2.imwrite("temp.png", tmp)
        ##########################################################


        '''global tmp'''
        tmp = Image.open('temp.png')
        # size = int(iw /1.1), int(ih /1.1)
        # tmp = tmp.resize(size)
        tmp = tmp.convert("RGBA")

        pixdata = tmp.load()

        width, height = tmp.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        '''global tmp
        tmp=cv2.imread(image_i[current_canvas].image_name)
        size = int(iw), int(ih)
        #image_i[current_canvas].angle+=10
        #tmp=tmp.rotate(image_i[current_canvas].angle, expand=True)
        cv2.imwrite("temp.png",tmp)
        tmp = Image.open('temp.png')
        #size = int(iw /1.1), int(ih /1.1)
        #tmp = tmp.resize(size)
        image_i[current_canvas].angle += 10
        tmp = tmp.rotate(image_i[current_canvas].angle, expand=True)
        tmp.save("temp.png")
        tmp=Image.open("temp.png")
        tmp = tmp.convert("RGBA")
        pixdata = tmp.load()
        width, height = tmp.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        ######################################
        print size
        tmp1 = cv2.imread(image_i[current_canvas].image_name)
        cv2.imwrite("temp.png", tmp1)'''
        # draw
        #tmp.save("temp.png","PNG", quality=100)
        img= ImageTk.PhotoImage(tmp)
        image_i[current_canvas].tk_image=img
        image_i[current_canvas].image_obj=canvas.create_image(image_i[current_canvas].initialx,image_i[current_canvas].initialy, image=img)
        #print image_i[current_canvas].initialx, image_i[current_canvas].initialy
        image_i[current_canvas].s_img=cv2.imread("temp.png")
        #global hull_area
        #hull_area = hull_area - image_i[current_canvas].area
        #image_i[current_canvas].area = func(image_i[current_canvas].s_img)
        #hull_area += image_i[current_canvas].area
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button-1>', image_i[current_canvas].focus)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button1-Motion>', image_i[current_canvas].move)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<ButtonRelease-1>', image_i[current_canvas].release)
        image_i[current_canvas].highlight()
        image_i[current_canvas].helper()
    text.delete("1.0", END)



def rotateacw():
    print 1

def deleteobj():
    if current_canvas>0:
        global canvas
        canvas.delete(image_i[current_canvas].image_obj)
        image_i[current_canvas] = 0

def generateXML():
    root = ET.Element("root")
    bg = ET.SubElement(root, "background")
    ET.SubElement(bg, "name").text = image_i[0].image_name
    global index
    print index
    for i in range(1, index):
        if image_i[i]!=0:
            obj = ET.SubElement(root, "object")
            ET.SubElement(obj, "name").text = image_i[i].image_name
            ET.SubElement(obj, "scale").text = str(image_i[i].scale)
            ET.SubElement(obj, "angle").text = str(image_i[i].angle)
            ET.SubElement(obj, "x").text = str(image_i[i].initialx)
            ET.SubElement(obj, "y").text = str(image_i[i].initialy)
    tree = ET.ElementTree(root)
    tree.write("file.xml")
    print "XML created"

def printName():
	print("akshay")
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
        self.scale=1.0
        self.angle=0.0
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos
        self.s_img = cv2.imread(image_name)
        self.tk_image = ImageTk.PhotoImage(
            file="{}{}".format(IMAGE_PATH, image_name))
        self.image_obj = canvas.create_image(
            xpos, ypos, image=self.tk_image)
        self.area=0.0
        global hull_area
        if self.image_id>0:
            canvas.tag_bind(self.image_obj, '<Button-1>', self.focus)
            canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
            canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
            self.area=func(self.s_img)
            hull_area += self.area
        self.move_flag = False
        self.mouse_xpos=0
        self.mouse_ypos=0
        self.diffx=0
        self.diffy=0
        self.to_delete=False
        self.del_obj=0

    def init(self, scale, angle):
        self.angle=angle
        print angle,scale
        self.scale=scale
        #print current_canvas, "#####"
        global canvas
        global image_i
        canvas.delete(image_i[self.image_id].image_obj)
        # cv2.imshow('a',image_i[current_canvas].s_img)
        qwe = cv2.imread(image_i[self.image_id].image_name)
        iw, ih = qwe.shape[0], qwe.shape[1]
        ################
        ###################################################
        global tmp
        tmp = cv2.imread(image_i[self.image_id].image_name)
        #image_i[current_canvas].scale *= 1.1
        size = int(ih * image_i[self.image_id].scale), int(iw * image_i[self.image_id].scale)
        print  size
        tmp = cv2.resize(tmp, size)
        imagem = cv2.bitwise_not(tmp)
        rotated = imutils.rotate_bound(imagem, image_i[self.image_id].angle)
        tmp = cv2.bitwise_not(rotated)
        cv2.imwrite("temp.png", tmp)
        ##########################################################


        '''global tmp'''
        tmp = Image.open('temp.png')
        # size = int(iw /1.1), int(ih /1.1)
        # tmp = tmp.resize(size)
        tmp = tmp.convert("RGBA")

        pixdata = tmp.load()

        width, height = tmp.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        ######################################
        # image_i[current_canvas].scale *= 1.1
        print size
        img = ImageTk.PhotoImage(tmp)
        image_i[self.image_id].tk_image = img
        # self.img=self.img.subsample(self,x,y=2)
        # print image_i[current_canvas].initialx,image_i[current_canvas].initialy
        # img = ImageTk.PhotoImage(file="C:/Users/Aditya Agrawal/PycharmProjects/untitled2/img2.png")
        image_i[self.image_id].image_obj = canvas.create_image(image_i[self.image_id].initialx,
                                                                image_i[self.image_id].initialy, image=img)
        # print image_i[current_canvas].initialx, image_i[current_canvas].initialy
        image_i[self.image_id].s_img = cv2.imread("temp.png")
        #global hull_area
        #hull_area = hull_area - image_i[current_canvas].area
        #image_i[current_canvas].area = func(image_i[current_canvas].s_img)
        #hull_area += image_i[current_canvas].area
        canvas.tag_bind(image_i[self.image_id].image_obj, '<Button-1>', image_i[self.image_id].focus)
        canvas.tag_bind(image_i[self.image_id].image_obj, '<Button1-Motion>', image_i[self.image_id].move)
        canvas.tag_bind(image_i[self.image_id].image_obj, '<ButtonRelease-1>', image_i[self.image_id].release)
        #image_i[current_canvas].highlight()
        #image_i[current_canvas].helper()

    def focus(self, event):
        #print 1
        global current_canvas, prev_canvas
        global canvas
        global image_i
        if (current_canvas==-1 and prev_canvas==-1):
            current_canvas = self.image_id
            print current_canvas, prev_canvas
            self.highlight()
            #print "*"
        elif (current_canvas!=self.image_id):
            prev_canvas=current_canvas
            current_canvas=self.image_id
            print current_canvas, prev_canvas
            self.highlight()
            if image_i[prev_canvas]!=0:
                image_i[prev_canvas].unhighlight()
        #current_canvas=self.image_id



    def highlight(self):
        global current_canvas
        global canvas
        global image_i
        im2 = self.s_img
        im2[np.where((im2 != [255, 255, 255]).all(axis=2))] = [0, 255, 0]
        cv2.imwrite("colored.png", im2)
        img = Image.open("colored.png")
        img = img.convert("RGBA")
        pixdata = img.load()
        width, height = img.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        img.save("colored.png", "PNG")
        self.tk_image = ImageTk.PhotoImage(file="colored.png")
        # canvas.delete(image_i[current_canvas].image_obj)
        self.del_obj=self.image_obj
        self.to_delete=True
        image_i[current_canvas].image_obj = canvas.create_image(self.initialx, self.initialy, image=self.tk_image)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button-1>', image_i[current_canvas].focus)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<Button1-Motion>', image_i[current_canvas].move)
        canvas.tag_bind(image_i[current_canvas].image_obj, '<ButtonRelease-1>', image_i[current_canvas].release)

    def helper(self):
        if self.to_delete==True:
            self.to_delete=False
            canvas.delete(self.del_obj)

    def unhighlight(self):
        global current_canva,prev_canvas
        global canvas
        global image_i
        im2 = self.s_img
        im2[np.where((im2 == [0, 255, 0]).all(axis=2))] = [0, 0, 0]
        #cv2.imshow("a",im2)
        cv2.imwrite("colored.png", im2)
        img = Image.open("colored.png")
        img = img.convert("RGBA")
        pixdata = img.load()
        width, height = img.size
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        img.save("colored.png", "PNG")
        self.tk_image = ImageTk.PhotoImage(file="colored.png")
        self.del_obj=self.image_obj
        #canvas.delete(image_i[current_canvas].image_obj)
        image_i[prev_canvas].image_obj = canvas.create_image(self.initialx, self.initialy, image=self.tk_image)
        canvas.tag_bind(image_i[prev_canvas].image_obj, '<Button-1>', image_i[prev_canvas].focus)
        canvas.tag_bind(image_i[prev_canvas].image_obj, '<Button1-Motion>', image_i[prev_canvas].move)
        canvas.tag_bind(image_i[prev_canvas].image_obj, '<ButtonRelease-1>', image_i[prev_canvas].release)
        canvas.delete(self.del_obj)

    def move(self, event):
        #print 2
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
            global current_canvas
            #print current_canvas
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y
            self.diffx=self.mouse_xpos-self.initialx
            self.diffy=self.mouse_ypos-self.initialy

    def release(self, event):
        #print 3
        '''self.move_flag = False
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
        count= cv2.countNonZero(img_bwa)'''
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

        '''for i in range(1,20):
            if image_i[i]!=0:
                if image_i[i].image_id!=self.image_id:
                    x_img = image_i[i].s_img
                    l_img[image_i[i].initialy - (x_img.shape[0] / 2):image_i[i].initialy - (x_img.shape[0] / 2) + x_img.shape[0],image_i[i].initialx - (x_img.shape[1] / 2):image_i[i].initialx - (x_img.shape[1] / 2) + x_img.shape[1]] = x_img
        #cv2.imshow("a",l_img)
        global hull_area
        if (func(l_img)>1.02*hull_area or func(l_img)<0.98*hull_area) or (count!=1494308):
        #if func(l_img)!=2:
            self.canvas.move(self.image_obj,
                             self.initialx-event.x + self.diffx, self.initialy-event.y + self.diffy)
        else:
            self.initialx=event.x-self.diffx
            self.initialy=event.y-self.diffy
        print func(l_img), hull_area'''

        self.move_flag = False
        # s_img = cv2.imread("smaller_image.png")
        l_img = cv2.imread("background.png")
        if self.diffx==0 and self.diffy==0:
            x_offset=self.initialx - (self.s_img.shape[1] / 2)
            y_offset=self.initialy - (self.s_img.shape[0] / 2)
        else:
            x_offset = event.x - self.diffx - (self.s_img.shape[1] / 2)
            y_offset = event.y - self.diffy - (self.s_img.shape[0] / 2)
        print x_offset, y_offset, self.s_img.shape
        x1=l_img
        x1[y_offset:y_offset + self.s_img.shape[0], x_offset:x_offset + self.s_img.shape[1]] = self.s_img
        # cv2.imshow("a", l_img)
        img1 = cv2.imread(image_i[0].image_name)
        img2 = x1
        img_bwa = cv2.bitwise_or(img1, img2)
        img_bwa = cv2.bitwise_not(img_bwa)

        img_bwa = cv2.cvtColor(img_bwa, cv2.COLOR_BGR2GRAY)
        count = cv2.countNonZero(img_bwa)
        #print count,"............."
        #cv2.imshow("a",img_bwa)

        for i in range(1, 20):
            if image_i[i] != 0:
                if image_i[i].image_id != self.image_id:
                    x_img = image_i[i].s_img
                    y1=cv2.imread("background.png")
                    y1[image_i[i].initialy - (x_img.shape[0] / 2):image_i[i].initialy - (x_img.shape[0] / 2) + x_img.shape[0],
                    image_i[i].initialx - (x_img.shape[1] / 2):image_i[i].initialx - (x_img.shape[1] / 2) + x_img.shape[1]] = x_img
                    img_bwa = cv2.bitwise_or(img2, y1)
                    img_bwa=cv2.bitwise_not(img_bwa)
                    #cv2.imshow("a", img2)
                    #cv2.imshow("b", y1)
                    #cv2.imshow("c", img_bwa)
                    img_bwa = cv2.cvtColor(img_bwa, cv2.COLOR_BGR2GRAY)
                    count = max(count,cv2.countNonZero(img_bwa))
                    #print count, "............."

        #print count
        if count>0:
        #if (count!=1494308):
        #if func(l_img)!=2:
            self.canvas.move(self.image_obj,
                             self.initialx-event.x + self.diffx, self.initialy-event.y + self.diffy)
        else:
            self.initialx=x_offset+(self.s_img.shape[1] / 2)
            self.initialy=y_offset+(self.s_img.shape[0] / 2)
        self.diffx=0
        self.diffy=0
        if self.to_delete==True:
            self.to_delete=False
            canvas.delete(self.del_obj)






image_i=[]
for i in range(20):
    image_i.append(0)
index=0
def bg_upload():
    uplod = Tk()
    uplod.withdraw()
    global filename
    global new_filename
    global groundfilled_img
    global index
    file_opt = options = {}
    options['initialdir'] = 'C:/Users/Aditya_Agrawal/Desktop/'
    filename = askopenfilename(**file_opt)
    if filename=="":
        return
    xyz=cv2.imread(filename)
    image_i[index] = CreateCanvasObject(canvas, filename, xyz.shape[1]/2, xyz.shape[0]/2, index)
    index=index+1
    #img_uplod = Image.open(filename)
    #img_uplod = img_uplod.resize((480, 480), Image.ANTIALIAS)
    #img_uplod1 = ImageTk.PhotoImage(img_uplod)
    #text.window_create(tk.END, window=tk.Label(text, image=img_uplod1))
    #w1 = Label(root, image=img_uplod1)
    #w1.image = img_uplod1
    print filename

def obj_upload():
    uplod = Tk()
    uplod.withdraw()
    global filename
    global new_filename
    global groundfilled_img
    global index
    file_opt = options = {}
    options['initialdir'] = 'C:/Users/Aditya_Agrawal/Desktop/'
    filename = askopenfilename(**file_opt)
    if filename=="":
        return
    image_i[index] = CreateCanvasObject(canvas, filename, 1700, 150, index)
    index = index + 1
    #img_uplod = Image.open(filename)
    #img_uplod = img_uplod.resize((480, 480), Image.ANTIALIAS)
    #img_uplod1 = ImageTk.PhotoImage(img_uplod)
    # text.window_create(tk.END, window=tk.Label(text, image=img_uplod1))
    #w1 = Label(root, image=img_uplod1)
    #w1.image = img_uplod1
    print filename

def convert():
    uplod = Tk()
    uplod.withdraw()
    global filename
    global new_filename
    global groundfilled_img
    global index
    global canvas
    global current_canvas, prev_canvas
    file_opt = options = {}
    options['initialdir'] = 'C:/Users/Aditya_Agrawal/Desktop/'
    filename = askopenfilename(**file_opt)
    if filename=="":
        return
    for i in range(0,index):
        if image_i[i]!=0:
            canvas.delete(image_i[i].image_obj)
            image_i[i] = 0
    index=0
    current_canvas=-1
    prev_canvas=-1
    tree = ET.parse(filename)
    root = tree.getroot()
    for i in range(0, len(root)):
        if i==0:
            filename=root[i][0].text
            xyz = cv2.imread(filename)
            image_i[index] = CreateCanvasObject(canvas, filename, xyz.shape[1]/2, xyz.shape[0]/2, index)
            index=index+1
        else:
            image_i[index] = CreateCanvasObject(canvas, root[i][0].text , int(root[i][3].text), int(root[i][4].text), index)
            image_i[index].init(float(root[i][1].text), float(root[i][2].text))
            index = index + 1

#----------------------------------------------------------------------------------------------------------------------------------
root=tk.Tk()
root.wm_title("FLOOR PLANNER")
canvas = tk.Canvas(root, width=1882, height=794, bg='white',
                            highlightthickness=0)
canvas.pack(side="left",expand=True)
menubar=Menu(root)
subMenu=Menu(menubar,tearoff=0 )
menubar.add_cascade(label="File" , menu=subMenu)
subMenu.add_command(label="New" , command=bg_upload)
subMenu.add_command(label="Add object" , command=obj_upload)
subMenu.add_command(label="Load XML" , command=convert)
subMenu.add_separator()
subMenu.add_command(label="Exit" , command=exit)

#----------------------------------------------------------------------------------------------------------------------------------

tk.Button(root, text = "Zoom In current object", command=zoomin).place(x=80,y=20)
tk.Button(root, text = "Zoom Out current object", command=zoomout).place(x=280,y=20)
tk.Button(root, text = "Rotate current object", command=rotatecw).place(x=600,y=20)
text=tk.Text(root, height=1, width=5)
text.place(x=550,y=20)
#tk.Button(root, text = "Rotate ACW current object", command=rotateacw).place(x=680,y=20)
tk.Button(root, text = "Delete current object", command=deleteobj).place(x=840,y=20)
tk.Button(root, text = "Generate XML", command=generateXML).place(x=1040,y=20)

root.config(menu=menubar)
root.geometry("1000x750")
root.configure(background='#f5f5f5')
root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------

