#!/usr/bin/env python3

#Took me maybe an hour or two for both parts?

import sys
import time
import math

def main(arg):
    global debug
    debug = False
    
    if len(arg) != 0:
        if arg[0] == "debug":
            debug = True  

    start=time.time()

    sensors = getData("advent19a.txt")
    
    for s in sensors:
        for b1 in range(len(s.beacons)-1): #loop through each beacon except the last
            for b2 in range(b1+1,len(s.beacons)): #loop through all the beacons after the one selected above as b1
                
                s.distances.append(distance from b1 to b2) #add distance between beacons to list of distances for this sensor
     
    end=time.time()
      
    #print("Magnitude: " + str(maxMagnitude))
    #print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    if not debug:
        file = open(filename, "r")
        fileData = file.readlines()
    
    if debug:
        fileData = ["--- scanner 0 ---",
                    "0,2",
                    "4,1",
                    "3,3",
                    "",
                    "--- scanner 1 ---",
                    "-1,-1",
                    "-5,0",
                    "-2,1"]
   
    sensors = []
    currentSensor = -1
    for line in fileData:
        if "scanner" in line:
            currentSensor+=1
            sensors.append(Sensor(currentSensor))
        elif line == "":
            continue
        else:
            sensors[currentSensor].addBeacon(line)
            
    #for s in sensors:
    #    for b in s.beacons:
    #        b.printCoordinates()
        
    return sensors
    
def concatList(list):
    string=""
    for s in list:
        string+=s
    return string
      
class Sensor:
    def __init__(self, number):
        self.name = number
        self.beacons=[]
        self.distances=[]
        
    def addBeacon(self,coordinates):
        coordinateList = coordinates.split(",")
        
        self.beacons.append(Beacon(coordinateList[0],coordinateList[1],"z"))#,coordinateList[2]))
        
class Beacon:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def printCoordinates(self):
        coordinates = self.x + "," + self.y + "," + self.z
        print(coordinates)
    
if __name__ == '__main__':
    main(sys.argv[1:])
    
