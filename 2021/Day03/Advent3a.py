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

file = open("advent3a.txt", "r")
binaries = file.readlines()

#binaries=["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

numberofones = []
gamma = ""
epsilon = ""

binarylength = len(binaries[0].strip())

counter=0
while counter < binarylength:
    numberofones.append(0)
    counter+=1

#get the number of ones for each column
for binary in binaries:
    binary=binary.strip()
    
    digit = 0
    for bit in binary:
        numberofones[digit]+=int(bit)
        digit+=1

#create gamma and epsilon
for digit in numberofones:
    if digit > len(binaries)/2:
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"

decimalgamma = binaryToDecimal(int(gamma))
decimalepsilon = binaryToDecimal(int(epsilon))

print("length of list: "+str(len(binaries)))
print("length of binary: "+str(len(binaries[0].strip())))
    
print ("\nGamma: "+gamma+"\nEpsilon: "+epsilon)
print ("\nGamma: "+str(decimalgamma)+"\nEpsilon: "+str(decimalepsilon))
print ("Answer: " + str(decimalgamma*decimalepsilon))