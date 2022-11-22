#!/usr/bin/env python3

import time
import re

def main():
    start=time.time()

    target = getData("advent17a.txt")
    
    probe = Probe()
    
    maxHeight=0
    maxVelocity=0,0
    for x in range(1,100):
        for y in range(100):
            probe.setVelocity(x,y)
            for s in range(1000):
                probe.move()
                probe.drag()
                probe.gravity()

                if target.inArea(probe.x,probe.y):
                    if maxHeight < max(probe.yPositions):
                        maxHeight = max(probe.yPositions)
                        maxVelocity = x,y
                    break
                if probe.x > target.highX or probe.y < target.lowY:
                    break
            probe.reset()
         
    end=time.time()
      
    print("Max height: " + str(maxHeight))
    print("best Velocity: " + str(maxVelocity))
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
    
    
def Display(probe,TargetArea):
    return True
    
 
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
    global debug
    debug = False

    main()
    
