import Tkinter as tk
from Tkinter import *
import ttk
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
import coverage
from retrieval import *
from ski1 import *
from graph import *



def create_window(filename,new_filename,root):

    master = tk.Toplevel(root)

    label1 = Label(master, bg="black", height=55, width=60)
    label1.place(x=0, y=0)

    label2 = Label(master, bg="#574395", height=55, width=5)
    label2.place(x=400, y=0)

    label3 = Label(master, bg="#a4d5f3", height=55, width=160)
    label3.place(x=410, y=0)
    OPTIONS = [
		"1",
		"2",
		"3",
		"4",
		"5",
		"6"
	]

    # master = tk.Tk()
    variable = StringVar(master)
    variable.set(OPTIONS[0])  # default value

    w = apply(OptionMenu, (master, variable) + tuple(OPTIONS))
    master.geometry("1520x760")

    # ttk.Separator(master, orient=VERTICAL).grid(column=5, rowspan=5,sticky="ew")
    # ttk.Separator(master, orient=VERTICAL).place(x=500, y=50)
    # C = Canvas(master)
    # C.create_line(0, 0, 0, 100)
    # C.pack()




    txt1 = tk.Text(master, height=17, width=35)
    txt1.place(x=50, y=30)

    label4 = Label(master, bg="#574395", height=2, width=30,text="QUERY IMAGE",foreground="WHITE" , font=("Helvetica 9 bold"))
    label4.place(x=90, y=330)

    label5 = Label(master, bg="#574395", height=2, width=30,text="GRAPH",foreground="WHITE" , font=("Helvetica 9 bold"))
    label5.place(x=90, y=680)

    label6 = Label(master, bg="#574395", height=2, width=30,text="SHOW RANK ORDERED IMAGES",foreground="WHITE" , font=("Helvetica 9 bold"))
    label6.place(x=850, y=10)



    txt2 = tk.Text(master, height=17, width=35)
    txt2.place(x=50, y=380)
    img_uplod = Image.open(filename)
    img_uplod = img_uplod.resize((280, 270), Image.ANTIALIAS)
    img_uplod1 = ImageTk.PhotoImage(img_uplod)


    txt1.window_create(tk.END, window=tk.Label(txt1, image=img_uplod1))
    l1 = Label(master, image=img_uplod1)
    l1.image = img_uplod1

    im1 = cv2.imread('graph.tiff')
    res = cv2.resize(im1, (280, 270), interpolation=cv2.INTER_CUBIC)
    im2 = Image.fromarray(res)
    imgtkr = ImageTk.PhotoImage(image=im2)
    txt2.window_create(tk.END, window=tk.Label(txt2, image=imgtkr))
    w1 = Label(master, image=imgtkr)
    w1.image = imgtkr


    # txt3 = tk.Text(master, height=15, width=30)
    # txt3.place(x=1100, y=50)
    # txt4 = tk.Text(master, height=15, width=30)
    # txt4.place(x=500, y=400)
    # txt5 = tk.Text(master, height=15, width=30)
    # txt5.place(x=800, y=400)
    # txt6 = tk.Text(master, height=15, width=30)
    # txt6.place(x=1100, y=400)



    w.place(x=170,y=720)
    tk.Button(master, text="SHOW RANK ORDERED IMAGES", command=lambda: object_matching(filename,new_filename,master,variable),height=2,width=30 , fg="white",bg="#574395", activebackground="#6f602a").place(x=90, y=770)

    master.mainloop()

