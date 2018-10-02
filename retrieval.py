import Tkinter as tk
from Tkinter import *
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
from xl import *
import operator



def object_matching(filename,new_filename,master,variable):
    selected_no_of_image = variable.get()
    print filename
    ary1, len1 , large_arr1 = array_objects(filename, new_filename)
    print ary1,len1
    print large_arr1

    dictionary_large_arr1={}
    for k1 in range(0,len(ary1)):
        count=0
        for k2 in range(0,len(large_arr1)):
            if ary1[k1]==large_arr1[k2]:
                count=count+1
        dictionary_large_arr1[ary1[k1]]=count

    print dictionary_large_arr1.keys()
    print dictionary_large_arr1.values()
    a, b = filename.rsplit("_", 1)
    c, d = b.split(".")
    e,f=a.rsplit("/",1)
    e1,f1=e.rsplit("-",1)
    arr_of_objects=[]
    if f1!=str(1) and f1!=str(2):
        for i in range(0,21):

            a1,b1=new_filename.rsplit("_",1)
            c1,d1=b1.split(".")

            if int(c) != i:

                model_img = str(a) + "_" + str(i) + "." + str(d)

                model_img_xml = a1 + "_" + str(i) + "." + d1
                print model_img_xml

                ary2, len2 , large_arr2 = array_objects(model_img, model_img_xml)
                print ary2, len2
                dictionary_large_arr2 = {}
                for r1 in range(0, len(ary2)):
                    count = 0
                    for r2 in range(0, len(large_arr2)):
                        if ary2[r1] == large_arr2[r2]:
                            count = count + 1
                    dictionary_large_arr2[ary2[r1]] = count

                print dictionary_large_arr2.keys()
                print dictionary_large_arr2.values()
                print dictionary_large_arr2.get('rashi')
                diff_objs = 0

                common_set_of_unique_elements=set(ary1) | set(ary2)
                print common_set_of_unique_elements

                common_array_of_unique_elements = []
                k = 0
                for e in common_set_of_unique_elements:
                    common_array_of_unique_elements.append(e)
                    k = k + 1

                for j in range(0,len(common_array_of_unique_elements)):
                    element=common_array_of_unique_elements[j]
                    if (dictionary_large_arr1.get(element))==None:
                        diff_objs=diff_objs+dictionary_large_arr2.get(element)
                    elif (dictionary_large_arr2.get(element))==None:
                        diff_objs=diff_objs+dictionary_large_arr1.get(element)

                    else:
                        d=(dictionary_large_arr1.get(element))-(dictionary_large_arr2.get(element))
                        if d>=0:
                            diff_objs=diff_objs+d
                        else:
                            diff_objs=diff_objs-d

                print i
                arr_of_objects.append(diff_objs)


            else:
                arr_of_objects.append(1000)

    else:
        for i in range(1, 21):

            a1, b1 = new_filename.rsplit("_", 1)
            c1, d1 = b1.split(".")

            if int(c) != i:

                model_img = str(a) + "_" + str(i) + "." + str(d)

                model_img_xml = a1 + "_" + str(i) + "." + d1
                print model_img_xml

                ary2, len2, large_arr2 = array_objects(model_img, model_img_xml)
                print ary2, len2
                dictionary_large_arr2 = {}
                for r1 in range(0, len(ary2)):
                    count = 0
                    for r2 in range(0, len(large_arr2)):
                        if ary2[r1] == large_arr2[r2]:
                            count = count + 1
                    dictionary_large_arr2[ary2[r1]] = count

                print dictionary_large_arr2.keys()
                print dictionary_large_arr2.values()
                print dictionary_large_arr2.get('rashi')
                diff_objs = 0

                common_set_of_unique_elements = set(ary1) | set(ary2)
                print common_set_of_unique_elements

                common_array_of_unique_elements = []
                k = 0
                for e in common_set_of_unique_elements:
                    common_array_of_unique_elements.append(e)
                    k = k + 1

                for j in range(0, len(common_array_of_unique_elements)):
                    element = common_array_of_unique_elements[j]
                    if (dictionary_large_arr1.get(element)) == None:
                        diff_objs = diff_objs + dictionary_large_arr2.get(element)
                    elif (dictionary_large_arr2.get(element)) == None:
                        diff_objs = diff_objs + dictionary_large_arr1.get(element)

                    else:
                        d = (dictionary_large_arr1.get(element)) - (dictionary_large_arr2.get(element))
                        if d >= 0:
                            diff_objs = diff_objs + d
                        else:
                            diff_objs = diff_objs - d

                print i
                arr_of_objects.append(diff_objs)


            else:
                arr_of_objects.append(1000)

    print arr_of_objects
    final_dictionary={}
    for q in range(1,21):
        final_dictionary[q]=arr_of_objects[q-1]


    print final_dictionary.keys()
    print final_dictionary.values()

    sorted_final_dictionary=sorted(final_dictionary.items(), key=operator.itemgetter(1))
    print sorted_final_dictionary
    imag1=sorted_final_dictionary[0][0]
    imag2=sorted_final_dictionary[1][0]
    imag3=sorted_final_dictionary[2][0]
    imag4=sorted_final_dictionary[3][0]
    imag5=sorted_final_dictionary[4][0]
    imag6=sorted_final_dictionary[5][0]


    if selected_no_of_image==(str(1)):
        frame = Frame(master, relief=GROOVE, bg="gray",width=800, height=800)
        frame.place(x=630,y=70)
        imag1_0 = a + "_" + str(imag1) + ".tiff"
        imag1_1 = Image.open(imag1_0)
        imag1_1 = imag1_1.resize((700, 700), Image.ANTIALIAS)
        imag1_2 = ImageTk.PhotoImage(image=imag1_1)
        w = Label(frame, image=imag1_2)
        w.pack()
        w.configure(image=imag1_2)
        w.image = imag1_2

    elif selected_no_of_image==(str(2)):
        frame1 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame1.place(x=500, y=210)
        imag1_0 = a + "_" + str(imag1) + ".tiff"
        imag1_1 = Image.open(imag1_0)
        imag1_1 = imag1_1.resize((400, 400), Image.ANTIALIAS)
        imag1_2 = ImageTk.PhotoImage(image=imag1_1)
        w = Label(frame1, image=imag1_2)
        w.pack()
        w.configure(image=imag1_2)
        w.image = imag1_2


        frame2 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame2.place(x=1000, y=210)
        imag2_0 = a + "_" + str(imag2) + ".tiff"
        imag2_1 = Image.open(imag2_0)
        imag2_1 = imag2_1.resize((400, 400), Image.ANTIALIAS)
        imag2_2 = ImageTk.PhotoImage(image=imag2_1)
        w = Label(frame2, image=imag2_2)
        w.pack()
        w.configure(image=imag2_2)
        w.image = imag2_2


    elif selected_no_of_image==(str(3)):
        frame1 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame1.place(x=500, y=80)
        imag1_0 = a + "_" + str(imag1) + ".tiff"
        imag1_1 = Image.open(imag1_0)
        imag1_1 = imag1_1.resize((340, 340), Image.ANTIALIAS)
        imag1_2 = ImageTk.PhotoImage(image=imag1_1)
        w = Label(frame1, image=imag1_2)
        w.pack()
        w.configure(image=imag1_2)
        w.image = imag1_2


        frame2 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame2.place(x=1000, y=80)
        imag2_0 = a + "_" + str(imag2) + ".tiff"
        imag2_1 = Image.open(imag2_0)
        imag2_1 = imag2_1.resize((340, 340), Image.ANTIALIAS)
        imag2_2 = ImageTk.PhotoImage(image=imag2_1)
        w = Label(frame2, image=imag2_2)
        w.pack()
        w.configure(image=imag2_2)
        w.image = imag2_2


        frame3 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame3.place(x=760, y=450)
        imag3_0 = a + "_" + str(imag3) + ".tiff"
        imag3_1 = Image.open(imag3_0)
        imag3_1 = imag3_1.resize((340, 340), Image.ANTIALIAS)
        imag3_2 = ImageTk.PhotoImage(image=imag3_1)
        w = Label(frame3, image=imag3_2)
        w.pack()
        w.configure(image=imag3_2)
        w.image = imag3_2



    elif selected_no_of_image==(str(4)):
        frame1 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame1.place(x=600, y=100)
        imag1_0 = a + "_" + str(imag1) + ".tiff"
        imag1_1 = Image.open(imag1_0)
        imag1_1 = imag1_1.resize((300, 300), Image.ANTIALIAS)
        imag1_2 = ImageTk.PhotoImage(image=imag1_1)
        w = Label(frame1, image=imag1_2)
        w.pack()
        w.configure(image=imag1_2)
        w.image = imag1_2

        frame2 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame2.place(x=1000, y=100)
        imag2_0 = a + "_" + str(imag2) + ".tiff"
        imag2_1 = Image.open(imag2_0)
        imag2_1 = imag2_1.resize((300, 300), Image.ANTIALIAS)
        imag2_2 = ImageTk.PhotoImage(image=imag2_1)
        w = Label(frame2, image=imag2_2)
        w.pack()
        w.configure(image=imag2_2)
        w.image = imag2_2

        frame3 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame3.place(x=600, y=450)
        imag3_0 = a + "_" + str(imag3) + ".tiff"
        imag3_1 = Image.open(imag3_0)
        imag3_1 = imag3_1.resize((300, 300), Image.ANTIALIAS)
        imag3_2 = ImageTk.PhotoImage(image=imag3_1)
        w = Label(frame3, image=imag3_2)
        w.pack()
        w.configure(image=imag3_2)
        w.image = imag3_2

        frame4 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame4.place(x=1000, y=450)
        imag4_0 = a + "_" + str(imag4) + ".tiff"
        imag4_1 = Image.open(imag4_0)
        imag4_1 = imag4_1.resize((300, 300), Image.ANTIALIAS)
        imag4_2 = ImageTk.PhotoImage(image=imag4_1)
        w = Label(frame4, image=imag4_2)
        w.pack()
        w.configure(image=imag4_2)
        w.image = imag4_2
    elif selected_no_of_image==(str(5)):

        frame1 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame1.place(x=500, y=120)
        imag1_0 = a + "_" + str(imag1) + ".tiff"
        imag1_1 = Image.open(imag1_0)
        imag1_1 = imag1_1.resize((250, 250), Image.ANTIALIAS)
        imag1_2 = ImageTk.PhotoImage(image=imag1_1)
        w = Label(frame1, image=imag1_2)
        w.pack()
        w.configure(image=imag1_2)
        w.image = imag1_2

        frame2 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame2.place(x=800, y=120)
        imag2_0 = a + "_" + str(imag2) + ".tiff"
        imag2_1 = Image.open(imag2_0)
        imag2_1 = imag2_1.resize((250, 250), Image.ANTIALIAS)
        imag2_2 = ImageTk.PhotoImage(image=imag2_1)
        w = Label(frame2, image=imag2_2)
        w.pack()
        w.configure(image=imag2_2)
        w.image = imag2_2

        frame3 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame3.place(x=1100, y=120)
        imag3_0 = a + "_" + str(imag3) + ".tiff"
        imag3_1 = Image.open(imag3_0)
        imag3_1 = imag3_1.resize((250, 250), Image.ANTIALIAS)
        imag3_2 = ImageTk.PhotoImage(image=imag3_1)
        w = Label(frame3, image=imag3_2)
        w.pack()
        w.configure(image=imag3_2)
        w.image = imag3_2

        frame4 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame4.place(x=600, y=450)
        imag4_0 = a + "_" + str(imag4) + ".tiff"
        imag4_1 = Image.open(imag4_0)
        imag4_1 = imag4_1.resize((250, 250), Image.ANTIALIAS)
        imag4_2 = ImageTk.PhotoImage(image=imag4_1)
        w = Label(frame4, image=imag4_2)
        w.pack()
        w.configure(image=imag4_2)
        w.image = imag4_2

        frame5 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame5.place(x=930, y=450)
        imag5_0 = a + "_" + str(imag5) + ".tiff"
        imag5_1 = Image.open(imag5_0)
        imag5_1 = imag5_1.resize((250, 250), Image.ANTIALIAS)
        imag5_2 = ImageTk.PhotoImage(image=imag5_1)
        w = Label(frame5, image=imag5_2)
        w.pack()
        w.configure(image=imag5_2)
        w.image = imag5_2

    else:
        frame1 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame1.place(x=500, y=120)
        imag1_0 = a + "_" + str(imag1) + ".tiff"
        imag1_1 = Image.open(imag1_0)
        imag1_1 = imag1_1.resize((250, 250), Image.ANTIALIAS)
        imag1_2 = ImageTk.PhotoImage(image=imag1_1)
        w = Label(frame1, image=imag1_2)
        w.pack()
        w.configure(image=imag1_2)
        w.image = imag1_2

        frame2 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame2.place(x=800, y=120)
        imag2_0 = a + "_" + str(imag2) + ".tiff"
        imag2_1 = Image.open(imag2_0)
        imag2_1 = imag2_1.resize((250, 250), Image.ANTIALIAS)
        imag2_2 = ImageTk.PhotoImage(image=imag2_1)
        w = Label(frame2, image=imag2_2)
        w.pack()
        w.configure(image=imag2_2)
        w.image = imag2_2

        frame3 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame3.place(x=1100, y=120)
        imag3_0 = a + "_" + str(imag3) + ".tiff"
        imag3_1 = Image.open(imag3_0)
        imag3_1 = imag3_1.resize((250, 250), Image.ANTIALIAS)
        imag3_2 = ImageTk.PhotoImage(image=imag3_1)
        w = Label(frame3, image=imag3_2)
        w.pack()
        w.configure(image=imag3_2)
        w.image = imag3_2

        frame4 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame4.place(x=500, y=450)
        imag4_0 = a + "_" + str(imag4) + ".tiff"
        imag4_1 = Image.open(imag4_0)
        imag4_1 = imag4_1.resize((250, 250), Image.ANTIALIAS)
        imag4_2 = ImageTk.PhotoImage(image=imag4_1)
        w = Label(frame4, image=imag4_2)
        w.pack()
        w.configure(image=imag4_2)
        w.image = imag4_2

        frame5 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame5.place(x=800, y=450)
        imag5_0 = a + "_" + str(imag5) + ".tiff"
        imag5_1 = Image.open(imag5_0)
        imag5_1 = imag5_1.resize((250, 250), Image.ANTIALIAS)
        imag5_2 = ImageTk.PhotoImage(image=imag5_1)
        w = Label(frame5, image=imag5_2)
        w.pack()
        w.configure(image=imag5_2)
        w.image = imag5_2

        frame6 = Frame(master, relief=GROOVE, bg="gray", width=300, height=300)
        frame6.place(x=1100, y=450)
        imag6_0 = a + "_" + str(imag6) + ".tiff"
        imag6_1 = Image.open(imag6_0)
        imag6_1 = imag6_1.resize((250, 250), Image.ANTIALIAS)
        imag6_2 = ImageTk.PhotoImage(image=imag6_1)
        w = Label(frame6, image=imag6_2)
        w.pack()
        w.configure(image=imag6_2)
        w.image = imag6_2















