#!/usr/bin/env python3

import time
import concurrent.futures

#length
#    2:1
#    3:7
#    4:4
#    5:2,3,5
#    6:0,6,9
#    7:8
#

def decodeOutput(e):

    decodedOutput=""
    for output in e.output:
        outputLength = int(len(output))
        if outputLength == 2:
            decodedOutput+="1"
        elif outputLength == 3:
            decodedOutput+="7"
        elif outputLength == 4:
            decodedOutput+="4"
        elif outputLength == 5:
            decodedOutput+=e.nonUniqueKey[''.join(sorted(output))]
        elif outputLength == 6:
            decodedOutput+=e.nonUniqueKey[''.join(sorted(output))]
        elif outputLength == 7:
            decodedOutput+="8"
            
    return int(decodedOutput)
    
class entry:
    pattern=[]
    output=[]
    nonUniqueKey={}
    decodedOutput=0  

    def __init__(self, patternandoutput, output = None):
    
        if output is None:
            self.pattern=patternandoutput.strip().split(" | ")[0].split(" ")
            self.output=patternandoutput.strip().split(" | ")[1].split(" ")
        else:   
            self.pattern = patternandoutput
            self.output = output
        
        self.nonUniqueKey={}
        self.createNonUniqueKey()
        self.decodedOutput=self.decodeOutput()    
    
    #def __init__(self, pattern, output):
    #    self.pattern = pattern
    #    self.output = output
    #    self.nonUniqueKey={}
    #    self.createNonUniqueKey()
    #    self.decodedOutput=self.decodeOutput()
    
    def whereLengthIs(self,length):
        return [p for p in self.pattern if len(p) == length]
                
    def createNonUniqueKey(self):
        one=list(self.whereLengthIs(2)[0])
        four=list(self.whereLengthIs(4)[0])
        
        self.decodeFives(one,four)
        self.decodeSixes(one,four)       
    
    def decodeFives(self,one,four):
        fives=self.whereLengthIs(5)   

        if len(fives) == 0:
            return
        
        three=[f for f in fives if all(item in list(f) for item in one)][0]
        fives.remove(three)        
        
        fourMinusOne=[x for x in four if x not in one]
    
        five=[f for f in fives if all(item in list(f) for item in fourMinusOne)][0]
        fives.remove(five)
        
        self.nonUniqueKey[''.join(sorted(fives[0]))]="2"
        self.nonUniqueKey[''.join(sorted(three))]="3"
        self.nonUniqueKey[''.join(sorted(five))]="5"
        
    def decodeSixes(self,one,four):
        sixes=self.whereLengthIs(6)
        
        if len(sixes) == 0:
            return
        
        nine=[s for s in sixes if all(item in list(s) for item in four)][0]
        sixes.remove(nine)
        
        zero=[s for s in sixes if all(item in list(s) for item in one)][0]
        sixes.remove(zero)
        
        self.nonUniqueKey[''.join(sorted(zero))]="0"
        self.nonUniqueKey[''.join(sorted(sixes[0]))]="6"
        self.nonUniqueKey[''.join(sorted(nine))]="9"
        
    def decodeOutput(self):
        decodedOutput=""
        for output in self.output:
            outputLength = int(len(output))
            if outputLength == 2:
                decodedOutput+="1"
            elif outputLength == 3:
                decodedOutput+="7"
            elif outputLength == 4:
                decodedOutput+="4"
            elif outputLength == 5:
                decodedOutput+=self.nonUniqueKey[''.join(sorted(output))]
            elif outputLength == 6:
                decodedOutput+=self.nonUniqueKey[''.join(sorted(output))]
            elif outputLength == 7:
                decodedOutput+="8"
              
        return int(decodedOutput)    
        
#RULES:
#    0: length=6 and has all of length=2 (the ONE) but not all of length=4 (the FOUR)
#    1: length=2
#    2: length=5 and has one of (length=4 (the FOUR) - length=2 (the ONE)) 
#    3: length=5 and has both of length=2 (the ONE)
#    4: length=4
#    5: length=5 and has both of (length=4 (the FOUR) - length=2 (the ONE))
#    6: length=6 and has one of length=2 (the ONE)
#    7: length=3
#    8: length=7
#    9: length=6 and has all of length=4 (the FOUR)



file = open("advent8a.txt", "r")
patternandoutputs = file.readlines()

#patternandoutputs = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
#        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
#        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
#        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
#        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
#        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
#        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
#        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
#        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
#        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
        
#patternandoutputs = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]


#first method -> create list of entry classes then run them through the decoder    
start = time.time()  
outputSum=0    
entries = []
for patternandoutput in patternandoutputs:
    pattern=patternandoutput.strip().split(" | ")[0].split(" ")
    output=patternandoutput.strip().split(" | ")[1].split(" ")
    e = entry(pattern,output)
    entries.append(e)  
    
for e in entries:    
    outputSum += decodeOutput(e)
    
end = time.time()
time1 = end-start
result1 = outputSum
#first method end


#second method -> create list of entry classes then sum their decodedOutput   
start = time.time() 
outputSum=0    
entries = []
for patternandoutput in patternandoutputs:
    pattern=patternandoutput.strip().split(" | ")[0].split(" ")
    output=patternandoutput.strip().split(" | ")[1].split(" ")
    e = entry(pattern,output)
    entries.append(e)

outputSum=sum(e.decodedOutput for e in entries)

end = time.time()
time2 = end-start
result2 = outputSum
#second method end


#Third method -> loop through once and sum after each class has been created  
start = time.time()   
outputSum=0    
for patternandoutput in patternandoutputs:
    pattern=patternandoutput.strip().split(" | ")[0].split(" ")
    output=patternandoutput.strip().split(" | ")[1].split(" ")
    e = entry(pattern,output)
    outputSum+=e.decodedOutput

end = time.time()
time3 = end-start
result3 = outputSum
#Third method end 


#Fourth method -> use threading 
start = time.time()   
outputSum=0  
entries = []  
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        entries = executor.map(entry, patternandoutputs)

outputSum=sum(e.decodedOutput for e in entries)

end = time.time()
time4 = end-start
result4 = outputSum
#Fourth method end 


#print("Easy: " + str(len(entries) - hard)) only 9 were easy (all 4 output codes had unique lengths)
#print("Hard: " + str(hard)) 191 hard (not worth checking and not just immediately making the nonUniqueKey)
#print("Entries: " + str(len(entries)))     
        
print("Method 1 Result: " + str(result1)) 
print("Method 2 Result: " + str(result2)) 
print("Method 3 Result: " + str(result3)) 
print("Method 4 Result: " + str(result4))  
print("Method 1 Time: " + str(time1) + " seconds")  
print("Method 2 Time: " + str(time2) + " seconds")  
print("Method 3 Time: " + str(time3) + " seconds")  
print("Method 4 Time: " + str(time4) + " seconds")   

times=[time1,time2,time3,time4]
print("Fastest Method was " + str(times.index(min(times))+1))      
        
    
