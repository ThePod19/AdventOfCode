#!/usr/bin/env python3

#list = [199,200,208,210,200,207,240,269,260,263]

list = []
file = open("advent1a.txt", "r")
numbers = file.readlines()

for number in numbers:
    list.append(int(number))

counter = 2
msg = ""
increaseNumber = 0
decreaseNumber = 0
nochangeNumber = 0


while counter < len(list)-1:
    sum1 = list[counter]+list[counter-1]+list[counter-2]
    sum2 = list[counter+1]+list[counter]+list[counter-1]


    direction = " (no change)"
    if sum2 > sum1:
        direction = " (increased)"
        increaseNumber += 1
    elif sum2 < sum1:
        direction = " (decreased)"
        decreaseNumber += 1
    else:
        nochangeNumber += 1
        
    msg = str(sum1) + direction
    
    #print(msg)
    counter += 1
    
print ("\nReport:\nNumbers increased "+str(increaseNumber)+" times\nNumbers decreased "+str(decreaseNumber)+" times\nNumbers didn't change "+str(nochangeNumber)+" times\n")