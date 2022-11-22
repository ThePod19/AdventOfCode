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

    snailNums = getData("advent18a.txt")
    
    #x + y
    maxMagnitude = 0
    maxReduction=""
    for x in range(len(snailNums)):
        firstAdd = snailNums[x].strip()
        for y in range(len(snailNums)):
            #ignore adding a row to itself?
            if x==y:
                continue
            
            #add snail numbers together
            initialAddition = snailAddition(firstAdd,snailNums[y].strip())
            
            #reduce addition
            finalReduction = reduce(initialAddition)
        
            magnitude = getMagnitude(finalReduction, 4)
            if int(magnitude) > int(maxMagnitude):
                maxMagnitude = magnitude
                maxReduction = finalReduction
           
    if debug:
        expected = "[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]"
        print(expected)
        print(maxReduction)
        print("Success? " + str(expected == maxReduction))
           
    if debug:
        expected = "3993"
        print(expected)
        print(maxMagnitude)
        print("Success? " + str(expected == maxMagnitude))
     
    end=time.time()
      
    print("Magnitude: " + str(maxMagnitude))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    if not debug:
        file = open(filename, "r")
        fileData = file.readlines()
    
    if debug:
        #fileData = ["[[[[4,3],4],4],[7,[[8,4],9]]]","[1,1]"]
        fileData = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        
        
    #regex = re.compile("=(\S*),\D*=(\S*$)")
    #processedData = regex.findall(fileData)
        
    return fileData
      
def snailAddition(num1, num2):
    return "[" + num1 + "," + num2 + "]"
    
def reduce(sum):
    depth=0
    reduced = False
    
    for i in range(len(sum)):
        if sum[i] == "[":
            depth += 1
        elif sum[i] == "]":
            depth -= 1
            
        #if 5 pairs deep, explode pair        
        if depth == 5:
            #print("Explode")
            sum = explode(sum, i)
            reduced = True
            break
    
    if not reduced:
        for i in range(len(sum)):
            #if double digit number is found, split number
            if sum[i].isnumeric():
                if sum[i+1].isnumeric():
                    #print("Split")
                    sum = split(sum, i)
                    reduced = True
                    break
               
    if reduced:
        sum = reduce(sum)
        
    return sum
            
def explode(sum, i):
    #grab exploding pair
    closingIndex = sum.index("]",i)
    ePair = sum[i:closingIndex+1]

    #grab the left number and right number from the exploding pair
    ePair = ePair.replace("[","").replace("]","")
    lNum = ePair.split(",")[0]
    rNum = ePair.split(",")[1]
    
    #grab everything to the left and right of the exploding pair
    left = sum[:i]
    right = sum[closingIndex+1:]
    
    #Go left and find the first number to add the left number
    start = 0
    end = 0
    for x in range(len(left)-1,0,-1):
        #find the start of the next number to the left
        if left[x].isnumeric() and end == 0:
            end = x+1
        #find the end of the next number to the right after you found the start
        if end != 0 and (left[x] == "[" or left[x] == ","):
            start = x+1
        #increase the next number to the right and re-construct the sum
        if start != 0 and end != 0:
            left = left[:start] + str(int(left[start:end])+int(lNum)) + left[end:]
            break
            
    #Go right and find the first number to add the right number
    start = 0
    end = 0
    for x in range(0,len(right)):
        #find the start of the next number to the right
        if right[x].isnumeric() and start == 0:
            start = x
        #find the end of the next number to the right after you found the start
        if start != 0 and (right[x] == "]" or right[x] == ","):
            end = x
        #increase the next number to the right and re-construct the sum
        if start != 0 and end != 0:
            right = right[:start] + str(int(right[start:end])+int(rNum)) + right[end:]
            break
    
    #re-construct the sum
    sum = left + "0" + right
            
    return sum
    
def split(sum, i):
    #grab the splitting number
    num = int(sum[i]+sum[i+1])
    
    #grab everything to the left and right of the splitting number
    left = sum[:i]
    right = sum[i+2:]
    
    #re-construct the sum
    sum = left + "[" + str(math.floor(num/2)) + "," + str(math.ceil(num/2)) + "]" + right
    
    return sum
    
def getMagnitude(magnitude, currentDepth):
    depth=0
    for c in range(len(magnitude)):
        if c >= len(magnitude):
            break
    
        if magnitude[c] == "[":
            depth += 1
        elif magnitude[c] == "]":
            depth -= 1
            
        if depth == currentDepth:
            closingIndex = magnitude.index("]",c)
            pair = magnitude[c:closingIndex+1]
            values = pair.replace("[","").replace("]","").split(",")
            magnitude = magnitude[:c] + str( int(values[0])*3 + int(values[1])*2 ) + magnitude[closingIndex+1:]
            depth -= 1
        
    layers = len([b for b in magnitude if b == "["])
    if layers == 0:
        return magnitude
    else:
        magnitude = getMagnitude(magnitude,currentDepth-1)
         
    return magnitude
    
if __name__ == '__main__':
    main(sys.argv[1:])
    
