import Tkinter as tk
from Tkinter import *
import ttk
import xml.etree.ElementTree as ET
from PIL import Image,ImageTk
import cv2
import numpy as np
import time
import coverage
import matplotlib.cm as cm
from gaps_close import *




def show_graph(adjacency_matrix,text2,root,color,nodes):

    import networkx as nx
    import matplotlib.pyplot as plt

    # no_rows_cols=adjacency_matrix.shape()

    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)

    color1=[]
    for i in range(0,len(nodes)):
        d = '#%02x%02x%02x' % color[i]
        color1.append(d)
        print d
        # nx.draw_networkx_nodes(gr,pos,nodelist=[nodes[i]],node_color=d,node_size=500)
        gr.add_node(nodes[i], node_color=d)
    nx.draw_networkx(gr,nodelist=nodes,node_color=color1,node_size=1200,width=4)


    plt.axis('off')
    plt.savefig('graph.tiff')
    # im1=cv2.imread('graph.tiff')
    im2=Image.open('graph.tiff')
    im1=np.array(im2)

    res=cv2.resize(im1,(460,460),interpolation=cv2.INTER_CUBIC)
    im3=Image.fromarray(res)
    imgtkr=ImageTk.PhotoImage(image=im3)
    # cv2.imshow('biuds',im1)

    #right_frame=Frame(root,relief=SUNKEN,bg="gray")
    #right_frame.pack(side="right")

    #w=Label(right_frame,image=imgtkr)

    # text2.pack()
    # text2.configure(image=imgtkr)
    #w.pack()
    # text2.image = imgtkr

    text2.window_create(tk.END, window=tk.Label(text2, image=imgtkr))
    w1 = Label(root, image=imgtkr)
    w1.image = imgtkr

	#plt.show()



