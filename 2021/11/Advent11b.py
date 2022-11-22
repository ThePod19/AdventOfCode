#!/usr/bin/env python3

import time
    
class octopus:
    def __init__(self, e):
        self.flashed=False
        self.energy=e
        self.adjacent=[]
        
    def powerUp(self):
        if self.flashed == False:
            self.energy+=1
        
            if self.energy >= 10:
                self.flash()
                      
    def flash(self):
        self.flashed=True
        self.energy=0
        
        #process adjacent
        for o in self.adjacent:
            o.powerUp()
            
    def reset(self):
        self.flashed=False
            
    def strEnergy(self):
        return str(self.energy)
        
    def adjacentReport(self):
        report="Energy " + str(self.energy) + ": "
        for x in self.adjacent:
            report+=str(x.energy)
            report+=", "
            
        print(report)

class row:
    #creates row of points and sets each point's left and right points
    def __init__(self, octopuses):
        self.rowOctos = []
        leftOneOctopus=None
        leftTwoOctopus=None
        currentOctopus=None
        for p in range(len(octopuses)):
            currentOctopus = octopus(int(octopuses[p]))
            
            if leftOneOctopus is None:
                leftOneOctopus = currentOctopus
                continue
            
            #append E and W octopuses to previous octopus since we have created the octopuses to its left and right
            if leftTwoOctopus is not None:
                leftOneOctopus.adjacent.append(leftTwoOctopus)
            leftOneOctopus.adjacent.append(currentOctopus)
            self.rowOctos.append(leftOneOctopus)
            
            #Last octopus still needs to be processed
            if p == len(octopuses)-1:
                currentOctopus.adjacent.append(leftOneOctopus)
                self.rowOctos.append(currentOctopus)
            else:
                #save these two octopuses for next loop
                leftTwoOctopus=leftOneOctopus
                leftOneOctopus=currentOctopus
        
                
    #sets the point's up and down octopuses while also determining if its a low point            
    def process(self, upperRow, lowerRow): 
        for index in range(len(self.rowOctos)):
            #append NW, N, and NE octopuses
            if upperRow is not None:
                if index-1 >= 0:
                    self.rowOctos[index].adjacent.append(upperRow.rowOctos[index-1])
                if index+1 <= len(self.rowOctos)-1:
                    self.rowOctos[index].adjacent.append(upperRow.rowOctos[index+1])
                self.rowOctos[index].adjacent.append(upperRow.rowOctos[index])
                
            #append SW, S, and SE octopus
            if lowerRow is not None:
                if index-1 >= 0:
                    self.rowOctos[index].adjacent.append(lowerRow.rowOctos[index-1])
                if index+1 <= len(self.rowOctos)-1:
                    self.rowOctos[index].adjacent.append(lowerRow.rowOctos[index+1])
                self.rowOctos[index].adjacent.append(lowerRow.rowOctos[index])                             
            
        return self
    

#get file data
file = open("advent11a.txt", "r") #was accidentally opening advent9a >:(
octopusRowsFile = file.readlines()

#override file data with example data
#octopusRowsFile = ["5483143223","2745854711","5264556173","6141336146","6357385478","4167524645","2176841721","6882881134","4846848554","5283751526"]
  
#get start time
start=time.time()  


#go through all the lines saving the current row
    #this can start the list of adjacent with east and west
#process the previous row
    #this saves a list of adjacent octopus to each octopus (min = 3, max = 8)
    #gets all the adjacent or get (all adjacent - east - west)
    
#then start a loop for the days
#loop through each row
#loop through each octopus
    #octopus energy += 1
    #if octopus energy >= 10
        #octopus.flash()
            #this resets octopus energy to 0 and marks flashed as true
            #then recursion through adjacent octopus list .flash()

#count flashes
#reset flashed

octopi=[]
upOneRow=None
upTwoRow=None
currentRow=None
for index in range(len(octopusRowsFile)):
    currentRow = row(octopusRowsFile[index].strip())
    
    if upOneRow is None:
        upOneRow = currentRow
        continue
    
    #process one row back since we have created the row above and below it
    octopi.extend(upOneRow.process(upTwoRow, currentRow).rowOctos)
    
    #Last row still needs to be processed
    if index == len(octopusRowsFile)-1:
        octopi.extend(currentRow.process(upOneRow,None).rowOctos)
    else:
        #save these two rows for next loop
        upTwoRow=upOneRow
        upOneRow=currentRow

stepEveroneFlashed=0
step=1
while stepEveroneFlashed==0:   
    for octopus in octopi:
        if octopus.flashed == False:
            octopus.powerUp()
            
    #at the end of the step, count up flashes and reset flashed fish
    flashedOctopus=[o for o in octopi if o.flashed==True]
    
    #quit when everyone flashes
    #print("Step " + str(step) + ": " + str(len(flashedOctopus)) + " octopus flashed out of " + str(len(octopi)) + " total.")
    if len(flashedOctopus) == len(octopi):
        stepEveroneFlashed=step
        break
    
    for fo in flashedOctopus:
        fo.reset()
        
    step+=1
    
#get end time 
end=time.time()
 
print("Step when all octopus flashed: " + str(stepEveroneFlashed))
print("This took " + str(end-start) + " seconds")   
        
    
