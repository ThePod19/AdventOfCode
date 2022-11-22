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
     
    steps=10
    for s in range(steps):
        additions=[]
        subtractions=[]
        possiblePolys=[p for p in polyPairs if polyPairs[p] > 0]
        print(possiblePolys)
        for possiblePoly in possiblePolys:
            if possiblePoly in [r.material for r in rules]:
                newPair = possiblePoly[0] + [r.product for r in rules if r.material == possiblePoly][0]
                additions.append(UpdatedPair(newPair, polyPairs[possiblePoly]))
                newPair = [r.product for r in rules if r.material == possiblePoly][0] + possiblePoly[1]
                additions.append(UpdatedPair(newPair, polyPairs[possiblePoly]))
                subtractions.append(UpdatedPair(possiblePoly, polyPairs[possiblePoly]))
        
        
        for addition in additions:
            #print(addition.pair)
            polyPairs[addition.pair]+=addition.count
            
        for subtraction in subtractions:
            #print(subtraction.pair)
            polyPairs[subtraction.pair]-=subtraction.count
    
    polymerCount={}
    for pair in polyPairs:
        #print(pair + " = " + str(polyPairs[pair]))
        for polymer in pair:
            if polymer not in polymerCount.keys():
                polymerCount[polymer]=polyPairs[pair]
            else:
                polymerCount[polymer]+=polyPairs[pair]
    
    
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