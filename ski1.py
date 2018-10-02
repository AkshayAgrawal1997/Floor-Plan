import cv2
import imutils
from PIL import Image, ImageDraw
import sys
import math, random
from itertools import product
import numpy as np
from ufarray import *
import operator
from PIL import ImageFont
import numpy.linalg as linalg
import networkx as nx
import matplotlib.pyplot as plt

color=[]
lab=[]
nodes=[]
def find(lab1,p):
    f=0;
    for i in lab1:
        if i==p:
            f=1
            return 0
    if f==0:
        return 1
def run(img):
    data = img
    width, height = img.shape
 
    
    uf = UFarray()
 
    
    labels = {}
 
    for y, x in product(range(height-1), range(width-1)):
 
        
        if data[x, y] == 255 :
            pass
 
        
        elif y > 0 and data[x, y-1] == 0:
            labels[x, y] = labels[(x, y-1)]
 
        
        elif x+1 < width and y > 0 and data[x+1, y-1] == 0:
 
            c = labels[(x+1, y-1)]
            labels[x, y] = c
 
           
            if x > 0 and data[x-1, y-1] == 0:
                a = labels[(x-1, y-1)]
                uf.union(c, a)
 
           
            elif x > 0 and data[x-1, y] == 0:
                d = labels[(x-1, y)]
                uf.union(c, d)
 
        elif x > 0 and y > 0 and data[x-1, y-1] == 0:
            labels[x, y] = labels[(x-1, y-1)]
 
        
        elif x > 0 and data[x-1, y] == 0:
            labels[x, y] = labels[(x-1, y)]
 
        
        else: 
            labels[x, y] = uf.makeLabel()
 
    
    
    
    uf.flatten()
    c=0
    for i in range(0,len(uf.P)):
        flag=0
        for j in range(0,i):
            
            if uf.P[j]==uf.P[i]:
                flag=1
                break

        if flag==0:
            c=c+1
            
          
      
        
    k=0
    mat=[0 for x in range(c)]

    for i in range(0,len(uf.P)):
        flag=0
        for j in range(0,i):
            
            if uf.P[j]==uf.P[i]:
                flag=1
                break

        if flag==0:
            mat[k]=uf.P[i]
            k=k+1
    
    #for k in range(0,len(mat)):
     #   print mat[k]
   
   
    
 
    colors = {}

    
    output_img = Image.new("RGB", (width,height))
    #output_img.show()
    outdata = output_img.load()
    #print outdata

    for (x, y) in labels:
 
        
        component = uf.find(labels[(x, y)])

        
        labels[(x, y)] = component
 
        
        if component not in colors and labels[x,y]!=min(uf.P): 
            colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

        
        if labels[(x,y)]!=min(uf.P):
        	outdata[x, y] = colors[component]
        if labels[x,y]==min(uf.P):
        	outdata[x,y]=(255,255,255)

    return (labels, output_img,c,mat)

#
# def show_graph(adjacency_matrix):
#
#     import networkx as nx
#     import matplotlib.pyplot as plt
#
#     rows,cols = np.where(adjacency_matrix == 1)
#     edges = zip(rows.tolist(), cols.tolist())
#     gr = nx.Graph()
#     gr.add_edges_from(edges)
#
#     nx.draw_networkx(gr)
#
#     plt.show()

def main(img):
    
    #img=cv2.imread(im)

    kernel=np.ones((5,5),np.uint8)
    img=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY_INV)


    erosion=cv2.erode(thresh,kernel,iterations=1)
    mirror=cv2.flip(erosion,1)
    #(h,w)=mirror.shape[:2]
    #center=(w/2,h/2)
    #M=cv2.getRotationMatrix2D(center,90,1.0)
    #rotated=cv2.warpAffine(mirror,M,(w,h))




    (labels, output_img,l,mat_array) = run(mirror)
    adj_mat=[[0 for x in range(l)] for y in range(l)]
    print l
    #for i in range(0,l):
        #for j in range(0,l):
            #print adj_mat[i][j]

    X,Y=output_img.size
   # print X,Y
    width, height = output_img.size
    i=0
    j=0
    ini_lab=0

    outdata=output_img.load()

    #finding adjacency matrix
    inil=0
    i=0
    j=0
    for i in range(0,X-1):
        inil=0
        j=0
        for j in range(0,Y-1):

            if outdata[i,j]==(255,255,255):
                pass
            elif outdata[i,j]==(0,0,0):
                pass
            elif labels[i,j]!=inil:
                #print inil
                adj_mat[mat_array.index(labels[i,j])][mat_array.index(inil)]=1
                adj_mat[mat_array.index(inil)][mat_array.index(labels[i,j])]=1
                inil=labels[i,j]
                #print inil

            j=j+1
        i=i+1

    i=0
    j=0
    inil=0
    for j in range(0,Y-1):
        inil=0
        i=0
        for i in range(0,X-1):

            if outdata[i,j]==(255,255,255):
                pass
            elif outdata[i,j]==(0,0,0):
                pass
            elif labels[i,j]!=inil:
                #print inil
                adj_mat[mat_array.index(labels[i,j])][mat_array.index(inil)]=1
                adj_mat[mat_array.index(inil)][mat_array.index(labels[i,j])]=1
                inil=labels[i,j]
                #print inil

            i=i+1
        j=j+1


    for i in range(0,len(mat_array)):
        if adj_mat[0][i]==0:
            adj_mat[0][i]=1
            adj_mat[i][0]=1
    for i in range(len(adj_mat)):
        print adj_mat[i]

    #img=np.array(output_img)
    final=output_img.copy()
    for j in range(0, Y - 1):

        i = 0
        for i in range(0, X - 1):

            if outdata[i, j] == (0, 0, 0):
                pass
            elif find(lab, labels[i, j]):

                color.append(outdata[i, j])
                print labels[i, j]
                img = np.zeros((50, 50, 3), np.uint8)
                # Draw a diagonal blue line with thickness of 5 px
                # cv2.line(img,(0,0),(511,511),(255,0,0),5)
                # cv2.putText(img,'1', (5,22), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
                cv2.putText(img, str(mat_array.index(labels[i, j])), (20, 22), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255), 2)
                img1 = Image.fromarray(img)
                img2 = img1.rotate(90, expand=1)
                # im=Image.open('color.tiff')
                # final=im.copy()
                final.paste(img2, (i, j))
                # final.show()
                # font=1
                # f = font = ImageFont.truetype("arial.ttf", font)
                # draw = ImageDraw.Draw(output_img)
                # draw.text((x,y), str(mat_array.index(labels[x,y])), (0,0,0),f)
                # draw = ImageDraw.Draw(output_img)
                ##cv2.putText(img,str(mat_array.index(labels[x,y])), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
                lab.append(labels[i, j])

            i = i + 1
        j = j + 1

    print color
    for i in lab:
        nodes.append(mat_array.index(i))

    print nodes


    #show_graph(np.array(adj_mat))


    #output_img.show()


    rot = final.rotate( 270, expand=1 )
    #img = np.array(rot)

    #P = np.array(adj_mat)

    #D, V = linalg.eig(P)
    #print(D)
    #print(V)
    
    #for (x,y) in labels:
       #cv2.putText(img,str(mat.index(labels[x,y])), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))

    return rot,adj_mat,color,nodes


    
    #output_img.show()
    #rot.show()
    #rot.save('color_text.tiff')
    #show_graph(np.array(adj_mat))

    

if __name__ == "__main__": main()
