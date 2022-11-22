#!/usr/bin/env python3

import time
#import concurrent.futures

    
class point:
    isLowPoint=False 
    height=0
    left=None
    right=None
    up=None
    down=None
    inBasin=False

    def __init__(self, h):
        self.height = h
        
    def process(self, l, r):
        self.left = l
        self.right = r
        
        return self

class row:
    rowPoints=[]

    #creates row of points and sets each point's left and right points
    def __init__(self, points):
        self.rowPoints = []
        leftOnePoint=None
        leftTwoPoint=None
        currentPoint=None
        for p in range(len(points)):
            currentPoint = point(int(points[p]))
            
            if leftOnePoint is None:
                leftOnePoint = currentPoint
                continue
            
            #process one point back since we have created the point to its left and right
            self.rowPoints.append(leftOnePoint.process(leftTwoPoint, currentPoint))
            
            #Last point still needs to be processed
            if p == len(points)-1:
                #print("Last point in row: " + str(points[p]))
                self.rowPoints.append(currentPoint.process(leftOnePoint,None))
            else:
                #save these two points for next loop
                leftTwoPoint=leftOnePoint
                leftOnePoint=currentPoint
        
                
    #sets the point's up and down points while also determining if its a low point            
    def process(self, upperRow, lowerRow): 
        for index in range(len(self.rowPoints)):
            isLowPoint=True
            if upperRow is not None:
                #set point's up point
                self.rowPoints[index].up=upperRow.rowPoints[index]
                if self.rowPoints[index].up.height <= self.rowPoints[index].height:
                    isLowPoint=False
            if lowerRow is not None:
                #set point's down point
                self.rowPoints[index].down=lowerRow.rowPoints[index]
                if self.rowPoints[index].down.height <= self.rowPoints[index].height:
                    isLowPoint=False
            if self.rowPoints[index].left is not None: 
                if self.rowPoints[index].left.height <= self.rowPoints[index].height:
                    isLowPoint=False
            if self.rowPoints[index].right is not None:
                if self.rowPoints[index].right.height <= self.rowPoints[index].height:
                    isLowPoint=False                

            self.rowPoints[index].isLowPoint=isLowPoint    
            
        return self

def processBasin(point):
    basinSize=0
    
    point.inBasin = True
    basinSize+=1
    
    if point.up is not None and point.up.inBasin == False and point.up.height != 9:
        basinSize+=processBasin(point.up)
    if point.right is not None and point.right.inBasin == False and point.right.height != 9:
        basinSize+=processBasin(point.right)
    if point.down is not None and point.down.inBasin == False and point.down.height != 9:
        basinSize+=processBasin(point.down)
    if point.left is not None and point.left.inBasin == False and point.left.height != 9:
        basinSize+=processBasin(point.left)
    
    return basinSize
    

#get file data
file = open("advent9a.txt", "r")
lavaTubeRowsFile = file.readlines()

#override file data with example data
#lavaTubeRowsFile = ["2199943210","3987894921","9856789892","8767896789","9899965678"]
  
#get start time
start=time.time()  

lavaTubeRows=[]
upOneRow=None
upTwoRow=None
currentRow=None
for index in range(len(lavaTubeRowsFile)):
    currentRow = row(lavaTubeRowsFile[index].strip())
    
    if upOneRow is None:
        upOneRow = currentRow
        continue
    
    #process one row back since we have created the row above and below it
    lavaTubeRows.append(upOneRow.process(upTwoRow, currentRow))
    
    #Last row still needs to be processed
    if index == len(lavaTubeRowsFile)-1:
        lavaTubeRows.append(currentRow.process(upOneRow,None))
    else:
        #save these two rows for next loop
        upTwoRow=upOneRow
        upOneRow=currentRow
    
largestBasins=[]       
for row in lavaTubeRows:
    for point in row.rowPoints:
        #for each lowpoint
        if point.isLowPoint:
            #process that basin
            currentBasinSize = processBasin(point)
            
            #if length of largestbasin < 3
            if len(largestBasins) < 3:
                #append basin length
                largestBasins.append(currentBasinSize)
            else:
                #get largestBasins min value
                minBasin = min(largestBasins)
                #if min < length of current basin
                if currentBasinSize > minBasin:
                    #replace index of min with current basin length
                    largestBasins[largestBasins.index(minBasin)]=currentBasinSize
                
                      
#multiply largestBasin values together
print(largestBasins)    
result=1
for basin in largestBasins:
    result*=basin
          
 
#get end time 
end=time.time()
 
print("Result: " + str(result))
print("This took " + str(end-start) + " seconds")   
        
    
