#!/usr/bin/env python3

import time

def main():
    start=time.time()

    data = getData("advent16a.txt")
    
    #convert hexadecimal to binary
    fullBinary = hexToBinary(data)
    
    versions=[]
    while len(fullBinary) > 7:
        fullBinary,versions=process(fullBinary,versions)
        
    print(versions)
    result = sum(versions)
         
    end=time.time()
     
    print("Result: " + str(result))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    file = open(filename, "r")
    dataFromFile = file.read().strip()

    #dataFromFile = "D2FE28" #literal
    
    #dataFromFile = "38006F45291200" #operator length type 0
    
    #dataFromFile = "EE00D40C823060" #operator length type 1
    
    #dataFromFile = "8A004A801A8002F478"
    
    #dataFromFile = "620080001611562C8802118E34"
    
    #dataFromFile = "C0015000016115A2E0802F182340"
    
    #dataFromFile = "A0016C880162017C3686B18A3D4780"
    
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
        binary=round(binary/10)
        i+=1

    return decimal
        

def process(binary,versions):
    version = binaryToDecimal(binary[0:3])
    versions.append(version)
    
    type = binaryToDecimal(binary[3:6])

    if type == 4:
        binary,versions=literal(binary,versions)
    else:
        binary = binary[6:]
        lengthType = binary[0]
        
        if lengthType == "0":
            subLength = binaryToDecimal(binary[1:16])
            binary = binary[16:]
            
            beforeLength=len(binary)
            while len(binary) != beforeLength - subLength:
                binary,versions=process(binary,versions)
        else:
            packetCount = binaryToDecimal(binary[1:12])
            binary = binary[12:]
            
            for p in range(packetCount):
                binary,versions=process(binary,versions)
    
    return binary,versions
        
def literal(binary,versions):
    version = binaryToDecimal(binary[0:3])

    type = binaryToDecimal(binary[3:6])
    #types.append(type)

    binary = binary[6:]
    
    literal=""
    done=False
    while not done:
        bits = binary[0:5]
        literal+=bits[1:]
        
        binary=binary[5:]
        
        if bits[0] == "0":
            done = True
    
    #print(binaryToDecimal(literal))    
    return binary,versions
        
if __name__ == '__main__':
    main()