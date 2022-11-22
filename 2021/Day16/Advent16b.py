#!/usr/bin/env python3

import time
import numpy as np

def main():
    start=time.time()

    data = getData("advent16a.txt")
    
    #convert hexadecimal to binary
    fullBinary = hexToBinary(data)
    
    packetValues=[]
    nonZeroBits = [b for b in fullBinary if b == '1']
    while len(nonZeroBits) > 0: #len(fullBinary) > 7:
        fullBinary,packetValues=processPacket(fullBinary,packetValues)
        nonZeroBits = [b for b in fullBinary if b == '1']
         
    end=time.time()
      
    print("Result: " + str(packetValues))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    file = open(filename, "r")
    dataFromFile = file.read().strip()

    #dataFromFile = "D2FE28" #literal
    
    #dataFromFile = "38006F45291200" #operator length type 0
    
    #dataFromFile = "EE00D40C823060" #operator length type 1
    
    #dataFromFile = "C200B40A82" #1+2=3
    
    #dataFromFile = "04005AC33890" #6*9=54
    
    #dataFromFile = "880086C3E88112" #min is 7
    
    #dataFromFile = "CE00C43D881120" #max is 9
    
    #dataFromFile = "D8005AC2A8F0" #5 < 15 = 1
    
    #dataFromFile = "F600BC2D8F" #5 > 15 = 0
    
    #dataFromFile = "9C005AC2F8F0" #5 == 15 = 0
    
    #dataFromFile = "9C0141080250320F1802104A08" # 1+3 == 2*2 = 1
    
    return dataFromFile
    
def hexToBinary(hex):
    hexBinaryDict = {
        "0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111",
        "8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"
    }
    
    binary=""
    for h in hex:
        binary+=hexBinaryDict[h]
    
    return binary
        
def binaryToDecimal(binary):
    binary = int(binary)
    decimal = 0 
    
    i=0
    while binary > 0:
        digit = binary % 10
        decimal += digit * 2**i
        binary=binary//10
        i+=1
        
    #Was originally doing binary=round(binary/10)
    #This was messing up certain binary cause it was rounding up (didn't expect that)
    #The // operator does floor (always rounds down)

    return int(decimal)
        

def processPacket(binary,values): 
    type = binaryToDecimal(binary[3:6])

    binary = binary[6:]
    
    #print("Type=" + str(type))
    
    if type == 4:
        binary,values=processliteralPacket(binary,values)
    else:
        lengthType = binary[0]
        
        #Save off the values from outer packets so they don't effect the current packet
        previousValues = values
        values = []
        
        if(debug):
            if type == 0:
                typeString = "Sum"
            elif type == 1:
                typeString = "Product"
            elif type == 2:
                typeString = "Min"
            elif type == 3:
                typeString = "Max"
            elif type == 5:
                typeString = "Greater Than"
            elif type == 6:
                typeString = "Less Than"
            elif type == 7:
                typeString = "Equal" 
            print("Type:"+typeString)
        
        #What is the operator's length type
        if lengthType == "0":
            binary,values = processZeroOperatorPacket(binary,values)
        else:
            binary,values = processOneOperatorPacket(binary,values)
 
        #What type of operator is it
        value = processOperator(type,values)
        
        if(debug):
            print("Type:"+typeString+" -> "+ str(values) + " = " + str(value))
        
        #append the inner packet value to the end of outer values
        previousValues.append(int(value))
        values = previousValues
    
    return binary,values
    
        
def processliteralPacket(binary,values):
    literal=""
    done=False
    while not done:
        bits = binary[0:5]
        literal+=bits[1:]
        
        binary=binary[5:]
        
        if bits[0] == "0":
            done = True
    
    values.append(binaryToDecimal(literal))
    
    if(debug):
        print("Literal " + str(literal) + "=" + str(binaryToDecimal(literal)))
    
    return binary,values
    
    
def processZeroOperatorPacket(binary,values):
    subLength = binaryToDecimal(binary[1:16])
    binary = binary[16:]
    
    if(debug):
        print("Subpackets are "+str(subLength)+ " long")
    
    beforeLength=len(binary)
    while len(binary) != beforeLength - subLength:
        binary,values=processPacket(binary,values)
        
    return binary,values

def processOneOperatorPacket(binary,values):
    packetCount = binaryToDecimal(binary[1:12])
    binary = binary[12:]
    
    if(debug):
        print("Has "+str(packetCount)+ " in it")
    
    for p in range(packetCount):
        binary,values=processPacket(binary,values)
        
    return binary,values
    
def processOperator(type, values):
    if type == 0:
        value = sum(values)
    elif type == 1:
        #F$&# NUMPY .PROD()
        #Incorrectly calculated 
        #Type:Product
        #Subpackets are 80 long
        #Literal 11110101=245
        #Literal 11010101=213
        #Literal 00110001=49
        #Literal 00101001=41
        #Literal 11110110=246
        #Type:Product -> [245, 213, 49, 41, 246] = 20753814
        value = 1
        for v in values:
            value *= v
        
        #value = np.prod(np.array(values,dtype=int))
    elif type == 2:
        value = min(values)
    elif type == 3:
        value = max(values)
    elif type == 5:
        value = 1 if values[0] > values[1] else 0
    elif type == 6:
        value = 1 if values[0] < values[1] else 0
    elif type == 7:
        value = 1 if values[0] == values[1] else 0
        
    return value       
    
if __name__ == '__main__':
    global debug
    debug = False

    main()