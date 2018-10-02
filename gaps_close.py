import Tkinter as tk
from Tkinter import *
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time



from tkFileDialog import askopenfilename
import tkMessageBox
from ski1 import *


def gaps_close(groundfilled_img,filename,new_filename,text1):
    im=cv2.imread(groundfilled_img)
    img=cv2.imread(filename)
    tree = ET.parse(new_filename)
    root = tree.getroot()
    a, b = groundfilled_img.split(".")
    c,d,e=a.split("-")
    #root = ET.fromstring(country_data_as_string)
    print root.tag
    for child in root:
            print child.tag, child.attrib

    print groundfilled_img
    w1,h1,c1=im.shape
    print w1,h1
    w,h,c=img.shape
    print w,h
    xf=float(w1)/float(w);
    yf=float(h1)/float(h);
    print xf;
    print yf;
    for y in root.findall('ov'):
            for z in y.findall('o'):
                    for u in z.findall('gom.std.OSymbol'):
                        x0=int(float(u.get('x0'))*xf);
                        print x0;
                        x1=int(float(u.get('x1'))*xf);
                        y0=int(float(u.get('y0'))*yf);
                        y1=int(float(u.get('y1'))*yf);
                        label=u.get('label');
                        #im = cv2.drawContours(im,[box],0,(0,0,255),2)
                        #cv2.rectangle(im,(x0,y0),(x1,y1),(0,255,0),2);
                        #cv2.putText(im,label, (x0,y0), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

                        if(label=="door1")&(u.get('direction')=="0.0"):
                            cv2.line(im,(x0,y1-5),(x1,y1-5),(0,0,0),5)
                        elif(label=="door1")&(u.get('direction')=="90.0"):
                            cv2.line(im,(x0+5,y0),(x0+5,y1),(0,0,0),5)
                        elif(label=="door1")&(u.get('direction')=="180.0"):
                            cv2.line(im,(x0,y0+5),(x1,y0+5),(0,0,0),5)
                        elif(label=="door1")&(u.get('direction')=="270.0"):
                            cv2.line(im,(x1-5,y0),(x1-5,y1),(0,0,0),5)
                        elif(label=="window1")&(u.get('direction')=="270.0"):
                            cv2.line(im,(x0+7,y0),(x0+7,y1),(0,0,0),14)
                        elif(label=="window1")&(u.get('direction')=="180.0"):
                            cv2.line(im,(x0,y1-7),(x1,y1-7),(0,0,0),14)
                        elif(label=="window1")&(u.get('direction')=="90.0"):
                            cv2.line(im,(x1-8,y0),(x1-8,y1),(0,0,0),14)
                        if(label=="window1")&(u.get('direction')=="0.0"):
                            cv2.line(im,(x0,y0+8),(x1,y0+8),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="270.0"):
                            cv2.line(im,(x0+8,y0),(x0+8,y1),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="180.0"):
                            cv2.line(im,(x0,y0+5),(x1,y0+5),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="90.0"):
                            cv2.line(im,(x0+5,y0),(x0+5,y1),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="0.0"):
                            cv2.line(im,(x0,y1-5),(x1,y1-5),(0,0,0),14)
                        elif (label == "door2") & (u.get('direction') == "90.0"):
                            cv2.line(im, (x0 + 5, y0), (x0 + 5, y1), (0, 0, 0), 6)
                        elif (label == "door2") & (u.get('direction') == "180.0"):
                            cv2.line(im, (x0, y0 + 5), (x1, y0 + 5), (0, 0, 0), 6)
                        elif (label == "door2") & (u.get('direction') == "270.0"):
                            cv2.line(im, (x1 - 5, y0), (x1 - 5, y1), (0, 0, 0), 6)
                        elif (label == "door2") & (u.get('direction') == "0.0"):
                            cv2.line(im, (x0, y1 - 5), (x1, y1 - 5), (0, 0, 0), 6)

                        print x0


    for y in root.findall('av'):
            for z in y.findall('a'):
                    for u in z.findall('gom.std.OSymbol'):
                        x0=int(float(u.get('x0'))*xf);
                        x1=int(float(u.get('x1'))*xf);
                        y0=int(float(u.get('y0'))*yf);
                        y1=int(float(u.get('y1'))*yf);
                        label=u.get('label');
                        #im = cv2.drawContours(im,[box],0,(0,0,255),2)
                        #cv2.rectangle(im,(x0,y0),(x1,y1),(0,255,0),2);
                        #cv2.putText(im,label, (x0,y0), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

                        if(label=="door1")&(u.get('direction')=="0.0"):
                            cv2.line(im,(x0,y1-5),(x1,y1-5),(0,0,0),5)
                        elif(label=="door1")&(u.get('direction')=="90.0"):
                            cv2.line(im,(x0+5,y0),(x0+5,y1),(0,0,0),5)
                        elif(label=="door1")&(u.get('direction')=="180.0"):
                            cv2.line(im,(x0,y0+5),(x1,y0+5),(0,0,0),5)
                        elif(label=="door1")&(u.get('direction')=="270.0"):
                            cv2.line(im,(x1-5,y0),(x1-5,y1),(0,0,0),5)
                        elif(label=="window1")&(u.get('direction')=="270.0"):
                            cv2.line(im,(x0+7,y0),(x0+7,y1),(0,0,0),14)
                        elif(label=="window1")&(u.get('direction')=="180.0"):
                            cv2.line(im,(x0,y1-7),(x1,y1-7),(0,0,0),14)
                        elif(label=="window1")&(u.get('direction')=="90.0"):
                            cv2.line(im,(x1+8,y0),(x1+8,y1),(0,0,0),14)
                        if(label=="window1")&(u.get('direction')=="0.0"):
                            cv2.line(im,(x0,y0+8),(x1,y0+8),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="270.0"):
                            cv2.line(im,(x0+8,y0),(x0+8,y1),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="180.0"):
                            cv2.line(im,(x0,y0+5),(x1,y0+5),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="90.0"):
                            cv2.line(im,(x0+8,y0),(x0+8,y1),(0,0,0),14)
                        elif(label=="window2")&(u.get('direction')=="0.0"):
                            cv2.line(im,(x0,y1-5),(x1,y1-5),(0,0,0),14)
                        elif (label == "door2") & (u.get('direction') == "90.0"):
                            cv2.line(im, (x0 + 5, y0), (x0 + 5, y1), (0, 0, 0), 5)
                        elif (label == "door2") & (u.get('direction') == "180.0"):
                            cv2.line(im, (x0, y0 + 5), (x1, y0 + 5), (0, 0, 0), 5)
                        elif (label == "door2") & (u.get('direction') == "270.0"):
                            cv2.line(im, (x1 - 5, y0), (x1 - 5, y1), (0, 0, 0), 5)
                        elif (label == "door2") & (u.get('direction') == "0.0"):
                            cv2.line(im, (x0, y1 - 5), (x1, y1 - 5), (0, 0, 0), 5)
                        print x0




#-----------------------------------------------------------------------------------------------------------------------------

    var = main(im)
    return var



#.....................................................................................................................

    # im2 = Image.fromarray(rot1)


    # im2 = ImageTk.PhotoImage(image=im1)
    # text1.window_create(END, window=tk.Label(text1, image=im2))  # Example 2
    #
    # w.configure(image=im2)
    # w.image = im2

    #im2 = Image.open(im)
    # im2 = im2.resize((460, 460), Image.ANTIALIAS)
    # im3 = ImageTk.PhotoImage(im2)
    # text1.window_create(tk.END, window=tk.Label(text1, image=im3))
    # w1 = Label(root, image=im3)
    # w1.image = im3


    #cv2.imshow("image",im)
    #cv2.imwrite("gapclosed_image.tiff",im)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

