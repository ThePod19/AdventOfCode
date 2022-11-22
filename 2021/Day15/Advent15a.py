#!/usr/bin/env python3

import time
import numpy as np
import sys
import concurrent.futures as thread


def main():
    start=time.time()

    data = getData("advent15a.txt")
    
    #create cave AKA matrix of risk levels
    processData(data)

    #quickBestToSpot = np.zeros(globalCave.shape)
    #firstcolumn = 0
    #for r in range(globalCave.shape[0]):
    #    if r != 0:
    #        firstcolumn += globalCave[r][0]
    #    for c in range(globalCave.shape[1]):
    #        if c == 0:
    #            quickBestToSpot[r][c] = globalCave[r][c] + (0 if r == 1 else firstcolumn)
    #        else:
    #            quickBestToSpot[r][c] = globalCave[r][c] + quickBestToSpot[r][c-1]
    #
    #print(quickBestToSpot)
    
    #traverse cave
    #input is x, y, path length, best path length, and best path length to spot matrix
    #quickLowestRisk=traverseRecursionQuick(0,0,0,sys.maxsize)  
    #lowestRisk=traverseRecursionFull(0,0,0,quickLowestRisk,np.zeros(globalCave.shape))
    
    lowestRisk=traverseLoop()
    
    #executor = thread.ThreadPoolExecutor(max_workers=2)
    #downFirst = executor.submit(traverse,(1), (0), (0), (sys.maxsize),(np.zeros(globalCave.shape)))
    #rightFirst = executor.submit(traverse,(0), (1), (0), (sys.maxsize),(np.zeros(globalCave.shape)))   
    #lowestRisk=min(downFirst.result(),rightFirst.result())
    
         
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
    #create empty cave with 10 columns
    cave = np.empty((0,len(data[0])),int)
    
    for line in data:
    
        #split line into list of characters
        row=[int(r) for r in line]
        
        #append the list of characters as a row in the matrix
        cave = np.r_[cave,[row]]
        
        #no reason to ever go back to start so zero it out
        cave[0][0] = 0
       
    global globalCave
    globalCave = cave
        
        
#def traverseRecursionFull(x, y, risk, lowestRisk, bestToSpot):
#    #Add risk level unless its the start
#    if not(x==0 and y==0):
#        risk+=globalCave[x][y]
#    
#    #Quit path if there was a faster way to this spot
#    if bestToSpot[x][y] == 0 or risk < bestToSpot[x][y]:
#        bestToSpot[x][y] = risk
#    else:
#        return lowestRisk
#        
#    #print("X=" + str(x) + ",Y=" + str(y))
#    
#    #Quit path if at the bottom right or current risk is greater than lowest risk
#    if (x == globalCave.shape[0]-1 and y == globalCave.shape[1]-1) or risk > lowestRisk:
#        if risk < lowestRisk:
#            lowestRisk = risk
#            #print(lowestRisk)
#        return lowestRisk
#    else:
#        #traverse down unless you are at the bottom or there is already a better path to the next spot
#        if x != globalCave.shape[0]-1:
#            lowestRisk= traverseRecursionFull(x+1,y,risk,lowestRisk,bestToSpot)
#        #traverse right unless you are at the side or there is already a better path to the next spot
#        if y != globalCave.shape[1]-1:
#            lowestRisk = traverseRecursionFull(x,y+1,risk,lowestRisk,bestToSpot)
#            
#        #traverse up unless you are at the top or there is already a better path to the next spot
#        if x != 0 and y != 0 and y != globalCave.shape[1]-1:
#            lowestRisk = traverseRecursionFull(x-1,y,risk,lowestRisk,bestToSpot)
#        #traverse left unless you are at the side or there is already a better path to the next spot
#        if y != 0 and x != 0 and x != globalCave.shape[0]-1:
#            lowestRisk = traverseRecursionFull(x,y-1,risk,lowestRisk,bestToSpot)
#        
#    return lowestRisk

    
def traverseRecursionQuick(x, y, risk, lowestRisk):
    #Add risk level unless its the start
    if not(x==0 and y==0):
        risk+=globalCave[x][y]
        
    #Quit path if at the bottom right or current risk is greater than lowest risk
    if (x == globalCave.shape[0]-1 and y == globalCave.shape[1]-1) or risk > lowestRisk:
        if risk < lowestRisk:
            lowestRisk = risk
            #print(lowestRisk)
        return lowestRisk
    else:
        down=10
        right=10
        #traverse down unless you are at the bottom or there is already a better path to the next spot
        if x != globalCave.shape[0]-1:
            down=globalCave[x+1][y]
            
        #traverse right unless you are at the side or there is already a better path to the next spot
        if y != globalCave.shape[1]-1:
            right=globalCave[x+1][y]
        
        if down < right:
            lowestRisk = traverseRecursionQuick(x+1,y,risk,lowestRisk)  
        else:
            lowestRisk = traverseRecursionQuick(x,y+1,risk,lowestRisk)
               
    return lowestRisk
    
def traverseLoop():
    quickGuide = np.zeros(globalCave.shape)
    
    row=1
    column=1
    processOut=1
    while row < globalCave.shape[0]:    
        #process top row
        quickGuide[0][column]=globalCave[0][column]+quickGuide[0][column-1]
    
        #process leftmost column
        quickGuide[row][0]=globalCave[row][0]+quickGuide[row-1][0]
    
        #process in between top/left and diagonal
        for p in range(1,processOut):
            quickGuide[p][column]=globalCave[p][column]+min( [quickGuide[p][column-1],quickGuide[p-1][column]] )
    
            quickGuide[row][p]=globalCave[row][p]+min( [quickGuide[row][p-1],quickGuide[row-1][p]] )
    
        #process diagonal
        quickGuide[row][column]=globalCave[row][column]+min([quickGuide[row][column-1],quickGuide[row-1][column]])
    
        #Check going up
        reprocess=False
        if row > 1:
            for c in range(processOut):
                for r in range(processOut): 
                    if quickGuide[row-r][column-c] + globalCave[row-r-1][column-c] < quickGuide[row-r-1][column-c]:
                        quickGuide[row-r-1][column-c] = quickGuide[row-r][column-c] + globalCave[row-r-1][column-c]
                        if c > 0:
                            reprocess=True
             
            #If better path was discovered above, reprocess everything 
            if reprocess == True:
                for r in range(1,globalCave.shape[0]):
                    for c in range(1,globalCave.shape[1]): 

                        if quickGuide[r][c] > quickGuide[r][c-1] + globalCave[r][c]:
                            quickGuide[r][c] = quickGuide[r][c-1] + globalCave[r][c]
                            
                        if quickGuide[r][c] > quickGuide[r-1][c] + globalCave[r][c]:
                            quickGuide[r][c] = quickGuide[r-1][c] + globalCave[r][c]
                    
        row+=1
        column+=1
        processOut+=1
        
        
    print(quickGuide)
    return quickGuide[-1][-1] 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
if __name__ == '__main__':
    main()