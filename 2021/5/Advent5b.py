#!/usr/bin/env python3

import time

def processHorizontal(vents,x,minY,maxY):
    for y in range(minY,maxY+1):
        vents[x][y]+=1
               
def processVertical(vents,y,minX,maxX):
    for x in range(minX,maxX+1):
        vents[x][y]+=1
        
def processDiagonal(vents,x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        vents[x1][y1]+=1
    else:
        vents[x1][y1]+=1
        
        if x1 > x2:
            x1-=1
        else:
            x1+=1
            
        if y1 > y2:
            y1-=1
        else:
            y1+=1
            
        processDiagonal(vents,x1,y1,x2,y2)   

file = open("advent5a.txt", "r")
filelines = file.readlines()

#filelines = ["0,9 -> 5,9","8,0 -> 0,8","9,4 -> 3,4","2,2 -> 2,1","7,0 -> 7,4","6,4 -> 2,0","0,9 -> 2,9","3,4 -> 1,4","0,0 -> 8,8","5,5 -> 8,2"]

lines=[]
for fileline in filelines:
    fileline = fileline.strip().replace(" -> ", ",")
    lines.append(fileline.split(","))
    
#print(lines)  

dimension = 0
for line in lines:
    for coor in line:
        dimension = max(int(coor),int(dimension))
        
#print(str(dimension)) 

vents = []
for r in range(dimension+1):
    vents.append([])
    for c in range(dimension+1):
        vents[r].append(0)
        
#print(vents)

totalHTime=0
totalDTime=0
Htimes=0
Dtimes=0
for coor in lines:
    t=0
    x1 = int(coor[1])
    y1 = int(coor[0])
    x2 = int(coor[3])
    y2 = int(coor[2])
    
    if x1==x2:
        if y2 > y1:
            start = time.time()
            processHorizontal(vents,x1,y1,y2)
            end = time.time()
            t = end-start
            Htimes+=1
            totalHTime+=t
        else:
            start = time.time()
            processHorizontal(vents,x1,y2,y1)
            end = time.time()
            t = end-start
            Htimes+=1
            totalHTime+=t
    elif y1==y2: 
        if x2 > x1:
            processVertical(vents,y1,x1,x2)
        else:
            processVertical(vents,y1,x2,x1)
    else:
        start = time.time()
        processDiagonal(vents,x1,y1,x2,y2)
        end = time.time()
        t = end-start
        Dtimes+=1
        totalDTime+=t

overlaps=0
for r in range(dimension+1):
    #print(vents[int(r)])
    for c in range(dimension+1):
        if vents[int(r)][int(c)] > 1:
            overlaps+=1

print("Total H Lines: " + str(Htimes))
print("Average H time: " + str(totalHTime/Htimes))
print("Total D Lines: " + str(Dtimes))
print("Average D time: " + str(totalDTime/Dtimes))

print("Result: " + str(overlaps))        
        
        
        
    
