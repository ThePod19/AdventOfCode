#!/usr/bin/env python3

#list = [199,200,208,210,200,207,240,269,260,263]

list = []
file = open("advent1.txt", "r")
numbers = file.readlines()

for number in numbers:
    list.append(int(number))

counter = 0
msg = ""
increaseNumber = 0
decreaseNumber = 0
nochangeNumber = 0


while counter < len(list):
    if(counter == 0):
        msg = str(list[counter]) + " (N/A - no previous measurement)"

    else:
        direction = " (no change)"
        if list[counter] > list[counter-1]:
            direction = " (increased)"
            increaseNumber += 1
        elif list[counter] < list[counter-1]:
            direction = " (decreased)"
            decreaseNumber += 1
        else:
            nochangeNumber += 1
            
        msg = str(list[counter]) + direction
    
    #print(increaseNumber)
    counter += 1
    
print ("\nReport:\nNumbers increased "+str(increaseNumber)+" times\nNumbers decreased "+str(decreaseNumber)+" times\nNumbers didn't change "+str(nochangeNumber)+" times\n")