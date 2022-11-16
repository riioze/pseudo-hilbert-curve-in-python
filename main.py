from typing import List,Tuple
import tkinter as tk
from math import cos,sin,pi





Point = Tuple[float,float]
Batch = List[Point]






def hilbert(order:int,angle:int, origin: Point, size:float) -> Batch:
    if order == 1:
        x,y = origin
        r : Batch = [(x + size*dx, y+size*dy) for (dx, dy) in [(0.25,0.25),(0.25,0.75),(0.75,0.75),(0.75,0.25)]]



        return rotate(r,angle,origin,size)
        return r
    
    else:
        norder = order-1
        nsize = size/2
    
        
        x,y = origin
        o1 = x,y
        o2 = x,y+nsize
        o3 = x+nsize,y+nsize
        o4 = x+nsize,y

        return rotate(hilbert(norder,-1,o1,nsize)[::-1]+hilbert(norder,0,o2,nsize)+hilbert(norder,0,o3,nsize)+hilbert(norder,1,o4,nsize)[::-1],angle,origin,size)


def rotate(points:Batch,angle:int,origin:Point,size:float) -> Batch:

    xo,yo = origin
    cx = xo+size/2
    cy = yo+size/2


    r:Batch = []
    for p in points:
        px,py = p
        nx = cx + cos(angle*pi/2) * (px - cx) - sin(angle*pi/2) * (py - cy)
        ny = cy + sin(angle*pi/2) * (px - cx) + cos(angle*pi/2) * (py - cy)
        r.append((nx,ny))



    return r


def show(points:Batch,c:tk.Canvas):
    for i in range(len(points)-1):
        x1,y1 = points[i]
        x2,y2 = points[i+1]
        #print(points[i],points[i+1])
        c.create_line(x1,y1,x2,y2,fill='white')


root =  tk.Tk()
c = tk.Canvas(root,width=800,height=800,bg='black')
c.pack()
pts = hilbert(5,0,(0,0),800)
show(pts,c)




root.mainloop()

    