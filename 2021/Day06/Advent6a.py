#!/usr/bin/env python3

import time

def processFish(fish,newfish,f):
    if f == 0:
        newfish[6]+=fish[f]
        newfish[8]+=fish[f]
    else:
        newfish[f-1]+=fish[f]

file = open("advent6a.txt", "r")
filefish = file.readline().split(",")

#filefish = [3,4,3,1,2]

#print(filefish)

fish=[0,0,0,0,0,0,0,0,0]
for filefish in filefish:
    filefishvalue = int(filefish)
    fish[filefishvalue]+=1

#print(fish)

days = 256
for day in range(days):
    newfish=[0,0,0,0,0,0,0,0,0] 
    for f in range(len(fish)):
        processFish(fish,newfish,f)
    fish = newfish
    
print(fish)

totalfish = sum(fish)

print("Result: " + str(totalfish))        
        
        
        
    
