#!/usr/bin/env python3

import time
import numpy as np
import sys
import concurrent.futures as thread


def main():
    start=time.time()

    data = getData("advent15a.txt")
    
    #create cave AKA matrix of risk levels
    cave = processData(data)
    
    #set number of rows and columns in cave
    global rows
    rows=cave.shape[0]
    global columns
    columns=cave.shape[1]
    
    #create dictionary of coordinates and Pos objects
    positions={}
    for r in range(rows):
        for c in range(columns):
            positions[index(r,c)]=Pos(cave[r][c])
    
    #Connect all the Pos objects to their adjacent Pos objects
    for i in positions:
        positions[i].Connect(positions,i)
        
    #Set each Pos objects best route
    x=1
    while x < rows:
        #process current row
        for y in range(x):
            positions[index(x,y)].process()
        
        #process current column        
        for y in range(x):
            positions[index(y,x)].process()
        
        #process diagonal (needs to be last)
        positions[index(x,x)].process()
        
        x+=1
    
    #print out best route data if running smal test data
    if rows < 10:    
        for r in range(rows):
            line=""   
            for c in range(columns):
                line += str(positions[index(r,c)].bestRoute) + "\t"
            print(line)
         
    lowestRisk = positions[index(rows-1,columns-1)].bestRoute
         
    end=time.time()
     
    print("Result: " + str(lowestRisk))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    file = open(filename, "r")
    dataFromFile = file.read().splitlines()

    #dataFromFile = ["1163751742","1381373672","2136511328","3694931569","7463417111","1319128137","1359912421","3125421639","1293138521","2311944581"]
    
    #dataFromFile = ["09911","19111","19191","19191","11191"] #my example
    
    #dataFromFile = ["46441","22212","27957","12145","14128"] #5X5 start of puzzle input
    
    
    return dataFromFile
    

def processData(data):
    #create empty cave with "size of data" columns
    cave = np.empty((0,len(data[0])),int)
    
    for line in data:
    
        #split line into list of characters
        row=[int(r) for r in line]
        
        #append the list of characters as a row in the matrix
        cave = np.r_[cave,[row]]
        
    finalCave=cave
    #Create the first row of bigger 5x5 matrix
    for x in range(1,5):
        cave = cave + np.ones((cave.shape[0],cave.shape[1]),int)
        
        for r in range(cave.shape[0]):
            for c in range(cave.shape[1]):
                if cave[r][c] == 10:
                    cave[r][c] = 1
                       
        finalCave = np.append(finalCave, cave, axis=1) 
    
    #Create the other four rows of the bigger 5x5 matrix
    cave = finalCave
    for x in range(1,5):
        cave = cave + np.ones((cave.shape[0],cave.shape[1]),int)
        
        for r in range(cave.shape[0]):
            for c in range(cave.shape[1]):
                if cave[r][c] == 10:
                    cave[r][c] = 1
                       
        finalCave = np.append(finalCave, cave, axis=0)  

    print(finalCave.shape)
        
    #no reason to ever go back to start so zero it out
    finalCave[0][0] = 0
       
    return finalCave
    
def index(r,c):
    return str(r)+","+str(c)
    
class Pos:
    def __init__(self,r):
        self.risk=r
        self.up=None
        self.right=None
        self.down=None
        self.left=None
        self.bestRoute=0 #change to a big number
        
    def Connect(self,positions,coordinates):
        row = int(coordinates.split(",")[0])
        column = int(coordinates.split(",")[1])
    
        #Set Up
        if row != 0:
            self.up = positions[index(row-1,column)]
        
        #Set Right
        if column != columns-1:
            self.right = positions[index(row,column+1)]
            
        #Set Down
        if row != rows-1:
            self.down = positions[index(row+1,column)]
            
        #Set Left
        if column != 0:
            self.left = positions[index(row,column-1) ]
            
    def process(self):    
        #if at the top row, inital best route is coming from left
        if self.up == None:
            self.bestRoute = self.left.bestRoute + self.risk    
        #if at the far left row, inital best route is coming from above    
        elif self.left == None:
            self.bestRoute = self.up.bestRoute + self.risk
        else:
            #Is coming from the left or from above better?
            shorterRoute = min( [self.up.bestRoute , self.left.bestRoute] )
            self.bestRoute = shorterRoute + self.risk
            
            self.check()
        
    def check(self):
        #check moving up from here
        if self.up != None:
            if self.up.bestRoute > self.bestRoute + self.up.risk: 
                self.up.bestRoute = self.bestRoute + self.up.risk
                self.up.check()
  
        #check moving left from here
        if self.left != None:
            if self.left.bestRoute > self.bestRoute + self.left.risk: 
                self.left.bestRoute = self.bestRoute + self.left.risk
                self.left.check()
                
        #check moving right from here
        if self.right != None:
            if self.right.bestRoute > self.bestRoute + self.right.risk: 
                self.right.bestRoute = self.bestRoute + self.right.risk
                self.right.check()
                
        #check moving left from here
        if self.down != None:
            if self.down.bestRoute > self.bestRoute + self.down.risk: 
                self.down.bestRoute = self.bestRoute + self.down.risk
                self.down.check()
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
if __name__ == '__main__':
    main()