import Tkinter as tk
from Tkinter import *
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
from gaps_close import *


from tkFileDialog import askopenfilename
import tkMessageBox

filename = ""
new_filename = ""
groundfilled_img = ""
myarray=[]

def printName():
	print("rashi")

def window():
	tkMessageBox.showinfo('Solve','Solve Puzzle')
	answer=tkMessageBox.askquestion('Question 1','Do u know about image processing')
	if answer=='yes':
		print("rocking")

def fileupload():
	uplod = Tk()
	uplod.withdraw()
	global filename
	global new_filename
	global groundfilled_img
	global myarray
	file_opt = options = {}
	options['initialdir'] = 'C:/Program Files/MATLAB/R2010b/IITJ_old/GUI/Dataset/SESYD dataset/Floorplans/'
	filename =askopenfilename(**file_opt)
	img_uplod=Image.open(filename)
	img_uplod = img_uplod.resize((460, 460), Image.ANTIALIAS)
	img_uplod1 = ImageTk.PhotoImage(img_uplod)
	text.window_create(tk.END, window=tk.Label(text, image=img_uplod1))
	w1 = Label(root, image=img_uplod1)
	w1.image = img_uplod1
	print filename
	a,b=filename.split(".")
	new_filename=a+".xml"
	print new_filename
	c,d=filename.split("-")

	e,f=d.split("/")
	ground = c+"-"+e+"/"
	if int(e)<10:
		e='0'+e;
		groundfilled_img=ground+"groundfilled-"+e+".png"
		print groundfilled_img
	else:
		groundfilled_img=ground+"groundfilled-"+e+".png"
		print groundfilled_img
	myarray.append(groundfilled_img)
	myarray.append(filename)
	myarray.append(new_filename)
	print myarray[:]


#-------------------------------------------------------------------------------------------------------------

root=tk.Tk()

root.wm_title("FLOOR PALN ANALYSIS ")
menubar=Menu(root)

subMenu=Menu(menubar,tearoff=0 )
menubar.add_cascade(label="File" , menu=subMenu)
subMenu.add_command(label="click Me" , command=window)
subMenu.add_command(label="print...." , command=printName)
subMenu.add_separator()
subMenu.add_command(label="save" , command=printName)

editMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit" , menu=editMenu)
editMenu.add_command(label="hey" , command=printName)
editMenu.add_command(label="rashi..." , command=printName)
editMenu.add_command(label="save" , command=printName)
editMenu.add_command(label="plot" , command=printName)
root.config(menu=menubar)



#------------------------Tool-bar---------------------------------

toolbar=Frame(root,bg="PeachPuff")

insertbutton=Button(toolbar,text="Insert Image" , command=printName)
insertbutton.pack(side=LEFT, padx=2,pady=2)
printbutton=Button(toolbar,text="print" , command=printName)
printbutton.pack(side=LEFT)
toolbar.pack(side=TOP, fill=X)



#----------------------status-bar------------------------------

status=Label(root,text="morphological operations on images..................", relief=SUNKEN  , anchor=W)
status.pack(side=BOTTOM, fill=X)


tk.Button(root, text="Quit", command=root.quit).pack()


text = tk.Text(root, height=30,width=60)
text.place(x= 2 , y=100)
tk.Button(root, text = "Insert a Floor-Plan Image", command=fileupload).place(x=190,y=600)

print filename
text1 = tk.Text(root, height=30,width=60)
text1.place(x= 500 , y=100)
tk.Button(root, text = "Segmented Image", command = lambda: gaps_close(groundfilled_img,filename,new_filename,text1)).place(x=700,y=600)

tk.Button(root, text = "SEARCH", command = printName).place(x=730,y=650)



text2 = tk.Text(root, height=30,width=60)
text2.place(x= 1000 , y=100)
tk.Button(root, text = "Graph", command = printName).place(x=1220,y=600)

root.geometry("1520x750")
root.mainloop()