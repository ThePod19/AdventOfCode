#!/usr/bin/env python3

import time
import math

def main():
    start=time.time()

    data = getData("advent14a.txt")
    
    #add dots to paper and get list of folding instructions
    template, rules = processData(data)
    
    #create dictionary of rule pairs
    polyPairs={}
    for rule in rules:
        polyPairs[rule.material]=0
        
    #record the number of instances of each pair in template
    for i in range(len(template)-1):
        pair=template[i] + template[i+1]
        polyPairs[pair]+=1
     
    steps=40
    for s in range(steps):
        additions=[]
        subtractions=[]
        possiblePolys=[p for p in polyPairs if polyPairs[p] > 0]
        #print(possiblePolys)
        for possiblePoly in possiblePolys:
            if possiblePoly in [r.material for r in rules]:
            
                #remember to add start of pair plus the new middle character
                newPair = possiblePoly[0] + [r.product for r in rules if r.material == possiblePoly][0]
                additions.append(UpdatedPair(newPair, polyPairs[possiblePoly]))
                
                #remember to add the new middle character plus end of the pair
                newPair = [r.product for r in rules if r.material == possiblePoly][0] + possiblePoly[1]
                
                #remember to remove the pair we just placed a character in the middle of
                additions.append(UpdatedPair(newPair, polyPairs[possiblePoly]))
                subtractions.append(UpdatedPair(possiblePoly, polyPairs[possiblePoly]))
        
        #update count of pairs we created by adding a character to the middle
        for addition in additions:
            polyPairs[addition.pair]+=addition.count
          
        #update count of pairs we destroyed by adding a character to the middle
        for subtraction in subtractions:
            polyPairs[subtraction.pair]-=subtraction.count
    
    #count up the individual characters
    polymerCount={}
    for pair in polyPairs:
        for polymer in pair:
            if polymer not in polymerCount.keys():
                polymerCount[polymer]=polyPairs[pair]
            else:
                polymerCount[polymer]+=polyPairs[pair]
    
    #divide count by 2 round up since we are double counting characters
    maxPoly=max([math.ceil(polymerCount[p]/2) for p in polymerCount]) 
    minPoly=min([math.ceil(polymerCount[p]/2) for p in polymerCount]) 
        
    end=time.time()
     
    print("Result: " + str(maxPoly-minPoly))
    print("This took " + str(end-start) + " seconds")  
    

def getData(filename):
    file = open(filename, "r")
    dataFromFile = file.readlines()

    #dataFromFile = ["NNCB","","CH -> B","HH -> N","CB -> H","NH -> C","HB -> C","HC -> B","HN -> C","NN -> C","BH -> H","NC -> B","NB -> B","BN -> B","BB -> N","BC -> B","CC -> N","CN -> C"]
    
    return dataFromFile
    

def processData(data):
    template=data[0].strip()
    rules=[]
    
    #loop through insertion rules
    for i in range(2,len(data)):        
        rules.append(Rule(data[i].strip().split(" -> ")[0],data[i].strip().split(" -> ")[1]))
    
    return template, rules
    
class Rule:
    def __init__(self, material, product):
        self.material = material
        self.product = product
        
    def printRule(self):
        print(self.material + " -> " + self.product)

#this class stores the new pair being added to the template and how many of them are being added        
class UpdatedPair:
    def __init__(self, pair, count):
        self.pair = pair
        self.count = count
    
if __name__ == '__main__':
    main()