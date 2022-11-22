#!/usr/bin/env python3

import time
from statistics import mean
from statistics import median

start = time.time()



file = open("advent7a.txt", "r")
crabstr = file.readline().split(",")
crabs = [int(i) for i in crabstr]

crabs = [16,1,2,0,4,2,7,1,2,14]
crabs = [1,1,1,1,1,1,1,1,1,14]

#print(crabs)

#print(mean(crabs))
print(median(crabs))

column = median(crabs)

totalfuel=0
for crab in crabs:
    totalfuel+=abs(crab-column)

end = time.time()

print("Result: " + str(totalfuel))  
print("Time: " + str(end-start))      
        
        
        
    
