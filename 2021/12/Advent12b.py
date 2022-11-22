#!/usr/bin/env python3

import time
    
class cave:
    def __init__(self, name):
        self.name=name
        self.connections=[] #list of cave objects
        if name.isupper():
            self.isLarge=True
        else:
            self.isLarge=False
        
        
    def addConnection(self, newConnection):
        oldConnection = [c for c in self.connections if c.name == newConnection.name]
        if len(oldConnection) == 0:
            self.connections.append(newConnection)
            
    def printConnections(self):
        message= "Large " if self.isLarge else "Small "
        message+="Cave " + self.name + " connects to "
        for c in self.connections:
            message += c.name + ", "
            
        print(message)
        
def traverse(cave,path,paths):
    if cave.name == "end":
        path+=cave.name
        paths.append(path)
    else:
        path+=cave.name+","
    
        #collect list of visited small caves
        visitedCaves=path.split(",")
        visitedSmallCaves=[c for c in visitedCaves if c.islower()]

        #if number of visited small caves is the same as the number of distinct visited small caves then we haven't visited any small cave twice yet
        #hence visit every cave connected regardless of size
        if len(visitedSmallCaves) == len(list(set(visitedSmallCaves))):
            for cc in cave.connections: 
                if cc.name != "start": #go to all connections except start
                    traverse(cc,path,paths)
        else:     
            for cc in cave.connections: 
                if cc.name != "start" and (cc.name+"," not in path or cc.isLarge): #don't go to start and only go to large caves or small caves not yet visited 
                    traverse(cc,path,paths)
        
    return paths
        

#get file data
file = open("advent12a.txt", "r")
connectionsFromFile = file.readlines()

#override file data with example data
#connectionsFromFile = ["start-A","start-b","A-c","A-b","b-d","A-end","b-end"] #36 paths

#connectionsFromFile = ["dc-end","HN-start","start-kj","dc-start","dc-HN","LN-dc","HN-end","kj-sa","kj-HN","kj-dc"] #103 paths

#connectionsFromFile = ["fs-end","he-DX","fs-he","start-DX","pj-DX","end-zg","zg-sl","zg-pj","pj-he","RW-he","fs-DX","pj-RW","zg-RW","start-pj","he-WI","zg-he","pj-fs","start-RW"] #3509 paths
  
#get start time
start=time.time() 

caves=[]
#loop over file lines to create and connect all the cave objects
for connection in connectionsFromFile:
    connection=connection.strip()
    
    name1=connection.split("-")[0]
    name2=connection.split("-")[1]
    
    cave1=[c for c in caves if c.name==name1]
    cave2=[c for c in caves if c.name==name2]
    
    #Make new caves if they don't exist
    if len(cave1) == 0:
        newCave = cave(name1)
        cave1.append(newCave)
        caves.append(newCave) 
    if len(cave2) == 0:
        newCave = cave(name2)
        cave2.append(newCave)
        caves.append(newCave)
    
    #Connect caves    
    cave1[0].addConnection(cave2[0])
    cave2[0].addConnection(cave1[0]) 

#for c in caves:
    #c.printConnections()

startCave = [c for c in caves if c.name == "start"][0]        
paths=traverse(startCave,"",[])
#for p in paths:
#    print(p)  
    
#get end time 
end=time.time()
 
print("Number of paths: " + str(len(paths)))
print("This took " + str(end-start) + " seconds")   
        
    
