#!/usr/bin/env python3

import time
import numpy as np
import re

def main():
    start=time.time()

    data = getData("advent13a.txt")
    
    #add dots to paper and get list of folding instructions
    paper, folds = processData(data)
    
    print(paper.paper.shape)
    
    #process folds
    folds=[folds[0]]
    for fold in folds:
        paper.fold(fold)

    print(paper.paper)
        
    #dotCount = countDots(foldedPaper)    
        
    end=time.time()
     
    #print(foldedPaper)
    print("Number of dots: " + str(paper.numberofdots))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    file = open(filename, "r")
    dataFromFile = file.readlines()

    #dataFromFile = ["6,10\n","0,14","9,10","0,3","10,4","4,11","6,0","6,12","4,1","0,13","10,12","3,4","3,0","8,4","1,10","2,14","8,10","9,0","","fold along y=7","fold along x=5"]
    
    return dataFromFile
    

def processData(data):
    dots=[]
    folds=[]
    
    #loop through points
    processingDots=True
    for line in data:        
        #switch to processing folds once the empty line is hit
        if line.strip() == "":
            processingDots=False
            continue
        
        #create a Dot or Fold object
        #flipped x and y since numpy matix is (rows,columns)
        if processingDots:
            xy=line.strip().split(",")
            dots.append(Dot(xy[1],xy[0]))
        else:
            value = line.split("=")
            if "x" in line:
                folds.append(Fold("y",value[1]))
            else:
                folds.append(Fold("x",value[1]))
    
    #Find the max aka size of the paper
    maxX = max([dot.x for dot in dots])+1
    maxY = max([dot.y for dot in dots])+1
    
    #Create an empty piece of paper
    paper = Paper(maxX,maxY)
    
    #Add the dots to the paper
    for dot in dots:
        paper.addDot(dot.x,dot.y)
    
    return paper, folds
    
    
class Dot:
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)   

    def printDot(self):
        print("X=" + str(self.x) + ",Y=" + str(self.y))
    
    
class Fold:
    def __init__(self, axis, value):
        self.axis = axis
        self.coordinate = int(value)  

    def printFold(self):
        print("Fold along " + self.axis + "=" + str(self.coordinate))
        
class Paper:
    def __init__(self, rows, columns):
        self.paper=np.zeros( ( rows, columns ) )
        self.numberofdots = self.dotCount()
        
    def dotCount(self):
        dotNum = 0
        for row in self.paper:
            for point in row:
                if point > 0:
                    dotNum += 1
                    
        self.numberofdots = dotNum
    
    def addDot(self, x, y):
        self.paper[x][y]=1
        
    def fold(self, fold):
        if fold.axis == "x":
            #get rows above fold
            top = self.paper[0:fold.coordinate,:]
            
            #get rows below fold
            bottom = self.paper[fold.coordinate+1:self.paper.shape[0],:]
            
            #if the fold isn't perfect, add zero rows
            if (self.paper.shape[0]-1)/2 != fold.coordinate:
                #add zero rows to the top
                while top.shape[0] < bottom.shape[0]:
                    top=np.insert(top,0,np.zeros((1,top.shape[1])),axis=0)
                #add zero rows to the bottom
                while top.shape[0] > bottom.shape[0]:
                    bottom=np.append(bottom,np.zeros((1,bottom.shape[1])),axis=0)
                
            self.paper = top + np.flipud(bottom)               
            
        else:
            #get columns to the left of fold
            left = self.paper[:,0:fold.coordinate]

            #get columns to the right of fold
            right = self.paper[:,fold.coordinate+1:self.paper.shape[1]]
            
            #if the fold isn't perfect, add zero columns
            if (self.paper.shape[1]-1)/2 != fold.coordinate:
                #add zero columns to the far left
                while left.shape[1] < right.shape[1]:
                    left=np.insert(left,0,np.zeros((left.shape[0],1)),axis=1)
                #add zero columns to the far right
                while left.shape[1] > right.shape[1]:
                    right=np.append(right,np.zeros((left.shape[0],1)),axis=1)
            self.paper = left + np.fliplr(right)

        self.dotCount()
                
    
if __name__ == '__main__':
    main()