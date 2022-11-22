#!/usr/bin/env python3

import time
from statistics import mean
from statistics import median
from statistics import mode
import sys

start = time.time()



file = open("advent7a.txt", "r")
crabstr = file.readline().split(",")
crabs = [int(i) for i in crabstr]

#crabs = [16,1,2,0,4,2,7,1,2,14]

print(mean(crabs))

mean = round(mean(crabs))
median = int(median(crabs))

print("Mean: " + str(mean))
print("Median: " + str(median))
#print("Mode: " + str(mode(crabs)))

#column = round(mean(crabs))
startcolumn = 0
endcolumn = 0

if median < mean:
    startcolumn = median
    endcolumn = mean
else:
    startcolumn = mean
    endcolumn = median

bestcolumn=0
bestfuel=sys.maxsize
totalfuel=0
print(bestfuel)
for x in range(startcolumn, endcolumn+1):
    for crab in crabs:
        n=abs(crab-x)
        totalfuel+=(n*(n+1))/2
    
    if totalfuel < bestfuel:
        bestcolumn = x
    bestfuel = min(totalfuel,bestfuel)
    totalfuel=0

end = time.time()

print("Best Column: " + str(bestcolumn))
print("Result: " + str(bestfuel))  
print("Time: " + str(end-start))      
        
        
        
    
