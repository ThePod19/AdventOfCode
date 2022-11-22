#!/usr/bin/env python3

import time

    
class point:
    isLowPoint=False 
    height=0
    left=None
    right=None

    def __init__(self, h, l, r):
        self.height = h
        self.left = l
        self.right = r

class row:
    rowPoints=[]

    def __init__(self, points):
        self.rowPoints = []
        for p in range(len(points)):
            if p == 0:
                self.rowPoints.append(point(int(points[p]),None,int(points[p+1])))
            elif p == len(points)-1:
                self.rowPoints.append(point(int(points[p]),int(points[p-1]), None))
            else:
                self.rowPoints.append(point(int(points[p]),int(points[p-1]), int(points[p+1])))
            
    def process(self, upperRow, lowerRow):
        rowLowPoints=""
 
        for index in range(len(self.rowPoints)):
            if upperRow is not None:
                if upperRow.rowPoints[index].height <= self.rowPoints[index].height:
                    continue
            if lowerRow is not None:
                if lowerRow.rowPoints[index].height <= self.rowPoints[index].height:
                    continue
            if self.rowPoints[index].left is not None: 
                if self.rowPoints[index].left <= self.rowPoints[index].height:
                    continue
            if self.rowPoints[index].right is not None:
                if self.rowPoints[index].right <= self.rowPoints[index].height:
                    continue                

            self.rowPoints[index].isLowPoint=True
            rowLowPoints+=str(self.rowPoints[index].height)      
    
        return rowLowPoints


#get file data
file = open("advent9a.txt", "r")
lavaTubeRows = file.readlines()

#override file data with example data
#lavaTubeRows = ["2199943210","3987894921","9856789892","8767896789","9899965678"]
  
#get start time
start=time.time()  

allLowPoints=""
upOneRow=None
upTwoRow=None
currentRow=None
for index in range(len(lavaTubeRows)):
    currentRow = row(lavaTubeRows[index].strip())
    
    if upOneRow is None:
        upOneRow = currentRow
        continue
    
    #process one row back since we have created the row above and below it
    lowPoints = upOneRow.process(upTwoRow, currentRow)
    
    #Last row still needs to be processed
    if index == len(lavaTubeRows)-1:
        lowPoints += currentRow.process(upOneRow,None)
    else:
        #save these two rows for next loop
        upTwoRow=upOneRow
        upOneRow=currentRow
    
    allLowPoints += lowPoints
    
risklevel=0
for x in allLowPoints:
    risklevel+=(int(x)+1)
 
#get end time 
end=time.time()

#print("Low points: " + str(allLowPoints))   
print("Risk level: " + str(risklevel))  
print("This took " + str(end-start) + " seconds")   
        
    
