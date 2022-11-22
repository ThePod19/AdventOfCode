#!/usr/bin/env python3

import time

#class zero:
#    segmentnum=6
#    segments=["a","b","c","e","f","g"]
#    
#class one:
#    segmentnum=2
#    segments=["a","b","c","d","e","f","g"]
#    
#class two:
#    segmentnum=5
#    segments=["c","f"]
#
#class three:
#    segmentnum=5
#    segments=["a","c","d","f","g"]
#
#class four:
#    segmentnum=4
#    segments=["b","c","d","f"]
#
#class five:
#    segmentnum=5
#    segments=["a","b","d","f","g"]
#
#class six:
#    segmentnum=6
#    segments=["a","b","d","e","f","g"]
#
#class seven:
#    segmentnum=3
#    segments=["a","c","f"]
#
#class eight:
#    segmentnum=7
#    segments=["a","b","c","d","e","f","g"]
#
#class nine:
#    segmentnum=6
#    segments=["a","b","c","d","f","g"]  

class entry:
    pattern=[]
    output=[]

start = time.time()

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
        
entries = []
for patternandoutput in patternandoutputs:
    e = entry()
    e.pattern=patternandoutput.strip().split(" | ")[0].split(" ")
    e.output=patternandoutput.strip().split(" | ")[1].split(" ")
    entries.append(e)

print(len(entries))

uniqueNumbers=0
uniqueLengths = [2,3,4,7]
for entry in entries:
    print(entry.output)
    for output in entry.output:
        if int(len(output)) in uniqueLengths:
            uniqueNumbers+=1

#print(entries[0].pattern)
#print(entries[0].output)

end = time.time()

print("Result: " + str(uniqueNumbers))  
print("Time: " + str(end-start))      
        
        
        
    
