#!/usr/bin/env python3

def binaryToDecimal(n):
    result = 0
    
    digit = 0
    while n > 0:
        remainder = n % 10
        result += remainder * pow(2,digit)
        n = int(n)//10
        digit+=1
        
    return result
    
def getOxygen(list, digit):
    zeros=0
    ones=0
    for binary in list:
        if int(binary[digit]) == 0:
            zeros+=1
        else:
            ones+=1
        
        if zeros > len(list)/2:
            newList=filterList(list,digit,0)
            break;
        if ones >= len(list)/2:
            newList=filterList(list,digit,1)
            break;
    
    if len(newList)==1:
        return str(newList[0])
    else:
        result = getOxygen(newList,digit+1)
        
    return result    

def getCO2(list, digit):
    zeros=0
    ones=0
    for binary in list:
        if int(binary[digit]) == 0:
            zeros+=1
        else:
            ones+=1
        
        if zeros > len(list)/2:
            newList=filterList(list,digit,1)
            break;
        if ones >= len(list)/2:
            newList=filterList(list,digit,0)
            break;
    
    if len(newList)==1:
        return str(newList[0])
    else:
        result = getCO2(newList,digit+1)
        
    return result     
            
def filterList(list, digit, wantedBit):
    newList = []
    for item in list:
        if int(item[digit]) == int(wantedBit):
            newList.append(item)
    
    return newList
    

file = open("advent3a.txt", "r")
binaries = file.readlines()

#binaries=["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

numberofones = []
gamma = ""
epsilon = ""

oxygen = getOxygen(binaries,0)
decimalOxygen = binaryToDecimal(int(oxygen))
print("Oxygen: " + str(oxygen.strip()))
print("Oxygen: " + str(decimalOxygen))

co2 = getCO2(binaries,0)
decimalCO2 = binaryToDecimal(int(co2))
print("CO2: " + str(co2.strip()))
print("CO2: " + str(decimalCO2))

print("Answer: " + str(decimalOxygen * decimalCO2))