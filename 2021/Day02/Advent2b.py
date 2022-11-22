#!/usr/bin/env python3

list = []
file = open("advent2a.txt", "r")
directions = file.readlines()

for direction in directions:
    list.append(direction.strip())

#list=["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

counter = 0
horiz = 0
depth = 0
aim = 0

while counter < len(list):

    if "forward" in list[counter]:
        horiz += int(list[counter][-1])
        depth += aim * int(list[counter][-1])
    elif "up" in list[counter]:
        aim -= int(list[counter][-1])
    elif "down" in list[counter]:
        aim += int(list[counter][-1])

    counter += 1
    
print ("\nHorizontal Position: "+str(horiz)+"\nDepth: "+str(depth))
print ("Answer: " + str(horiz*depth))