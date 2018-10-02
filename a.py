import Tkinter as tk
from Tkinter import *
import ttk
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
import coverage
from gaps_close import *

from new_window import *
from graph import *




from tkFileDialog import askopenfilename
import tkMessageBox

filename = ""
new_filename = ""
groundfilled_img = ""


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








def show_segment():
	global adj
	img1,adj=gaps_close(groundfilled_img,filename,new_filename,text1)
	img2=np.array(img1)
	res=cv2.resize(img2,(460,460),interpolation=cv2.INTER_CUBIC)
	im=Image.fromarray(res)
	imgtk=ImageTk.PhotoImage(image=im)
	text1.window_create(tk.END, window=tk.Label(text1, image=imgtk))
	w1=Label(root,image=imgtk)
	w1.image=imgtk


def pr_curve():
	pr1=cv2.imread("A:/BTP Codes/pr_curve.tiff")
	cv2.imshow("Precision-Recall Plot",pr1)




#-------------------------------------------------------------------------------------------------------------

root=tk.Tk()

root.wm_title("FLOOR PALN ANALYSIS ")
menubar=Menu(root)

subMenu=Menu(menubar,tearoff=0 )
menubar.add_cascade(label="File" , menu=subMenu)
subMenu.add_command(label="PR-Curve" , command=pr_curve)
subMenu.add_command(label="click Me" , command=window)
subMenu.add_separator()
subMenu.add_command(label="save" , command=printName)

editMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit" , menu=editMenu)
editMenu.add_command(label="hey" , command=printName)
editMenu.add_command(label="rashi..." , command=printName)
editMenu.add_command(label="save" , command=printName)
editMenu.add_command(label="plot" , command=printName)

quitMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Quit" , menu=quitMenu)
quitMenu.add_command(label="quit" , command=root.quit)


root.config(menu=menubar)



#------------------------Tool-bar---------------------------------

# toolbar=Frame(root,bg="PeachPuff")
#
# insertbutton=Button(toolbar,text="Insert Image" , command=printName)
# insertbutton.p)ack(side=LEFT, padx=2,pady=2)
# printbutton=Button(toolbar,text="print" , command=printName)
# printbutton.pack(side=LEFT
# toolbar.pack(side=TOP, fill=X)


header1 = Image.open("header.jpg")
header1 = header1.resize((1520, 100), Image.ANTIALIAS)
header2 = ImageTk.PhotoImage(image=header1)


toolbar = Label(root,image=header2)
toolbar.pack(side=TOP, fill=X)

toolbar1 = Label(root,bg="#e3d4c1",height=2,width=71, text="QUERY   IMAGE",foreground="BLACK" , font=("Helvetica 9 bold italic"))
toolbar1.place(x=0,y=103)

toolbar2 = Label(root,bg="#e3d4c1",height=2,width=73, text="SEGMENTED   IMAGE",foreground="BLACK" , font=("Helvetica 9 bold italic"))
toolbar2.place(x=505,y=103)

toolbar3 = Label(root,bg="#e3d4c1",height=2,width=72, text="GRAPH",foreground="BLACK" , font=("Helvetica 9 bold italic"))
toolbar3.place(x=1025,y=103)

toolbar4 = Label(root,bg="#e5e5e5",height=37,width=218,)
toolbar4.place(x=0,y=140)

toolbar5 = Label(root,bg="#e5e5e5",height=4,width=218,)
toolbar5.place(x=0,y=700)




#----------------------status-bar------------------------------

status=Label(root,text="morphological operations on images..................", relief=SUNKEN  , anchor=W)
status.pack(side=BOTTOM, fill=X)



text = tk.Text(root, height=30,width=60)
text.place(x= 0 , y=140)
tk.Button(root, text = "INSERT A FLOOR-PLAN IMAGE", command=fileupload , height=1,width=45 , fg="white",bg="#6be7d8", activebackground="#e3d4c1").place(x=80,y=640)

print filename
text1 = tk.Text(root, height=30,width=60)
text1.place(x= 520 , y=140)
tk.Button(root, text = "SEGMENTED IMAGE", command = show_segment, height=1,width=45 , fg="white",bg="#6be7d8", activebackground="#e3d4c1").place(x=600,y=640)

tk.Button(root, text = "SEARCH", command=lambda: create_window(filename,new_filename,root), height=2,width=45 , fg="white",bg="#6be7d8", activebackground="#e3d4c1").place(x=600,y=710)



text2 = tk.Text(root, height=30,width=60)
text2.place(x= 1040 , y=140)
tk.Button(root, text = "GRAPH", command = lambda: show_graph(np.array(adj),text2,root), height=1,width=45 , fg="white",bg="#6be7d8", activebackground="#e3d4c1").place(x=1120,y=640)

root.geometry("1520x760")
root.mainloop()