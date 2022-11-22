#!/usr/bin/env python3

#Took me maybe an hour or two for both parts?

import sys
import time
import re

def main(arg):
    global debug
    debug = False
    
    if len(arg) != 0:
        if arg[0] == "debug":
            debug = True  

    start=time.time()

    target = getData("advent17a.txt")
    
    probe = Probe()
    
    options=[]
    for x in range(1,target.highX+1):
        for y in range(target.lowY,target.lowY * -1):
            probe.setVelocity(x,y)
            while True:
                probe.move()
                probe.drag()
                probe.gravity()

                if target.inArea(probe.x,probe.y):
                    options.append(str(x)+","+str(y))
                    break
                if target.pastArea(probe.x,probe.y):
                    break
            probe.reset()
         
     
    end=time.time()
    
    print(options)
      
    print("Velocity Options: " + str(len(options)))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    file = open(filename, "r")
    fileData = file.read().strip()
    
    if debug:
        fileData = "target area: x=20..30, y=-10..-5"
    
    regex = re.compile("=(\S*),\D*=(\S*$)")
    processedData = regex.findall(fileData)
    
    target = TargetArea(processedData[0][0],processedData[0][1])
    
    return target
    
 
class TargetArea:
    def __init__(self,x,y):
        self.lowX = int(x.split("..")[0])
        self.highX = int(x.split("..")[1])
        self.lowY = int(y.split("..")[0])
        self.highY = int(y.split("..")[1])
        
    def inArea(self,x,y):
        if (self.lowX <= x <= self.highX) and (self.lowY <= y <= self.highY):
            return True
        else:
            return False
            
    def pastArea(self,x,y):
        if x > self.highX or y < self.lowY:
           return True
        else:
            return False

class Probe:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocityX = 0
        self.velocityY = 0
        self.yPositions = []
        
    def reset(self):
        self.x = 0
        self.y = 0
        self.yPositions = []
        
    def setVelocity(self,vx,vy):
        self.velocityX = vx
        self.velocityY = vy
        
    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY
        self.yPositions.append(self.y)
        
    def drag(self):
        if self.velocityX > 0:
            self.velocityX -= 1
            
    def gravity(self):
        self.velocityY -= 1
        
    
if __name__ == '__main__':
    main(sys.argv[1:])
    
