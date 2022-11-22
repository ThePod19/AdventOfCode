#!/usr/bin/env python3

import time
from statistics import median
  
class Stack:
    def __init__(self):
        self.stack = []
      
    def add(self, data):
        self.stack.append(data)
        
    def peek(self):
        return self.stack[-1]
        
    def remove(self):
        return self.stack.pop()
        
    def length(self):
        return len(self.stack)
        
    def printStack(self):
        stackString=""
        for y in self.stack:
            stackString+=y
            
        print(stackString)
        
def scoreCorruptCharacter(symbol):
    if symbol == ")":
        return 3
    elif symbol == "]":
        return 57
    elif symbol == "}":
        return 1197
    elif symbol == ">":
        return 25137
        
def scoreAutoCompleteCharacter(symbol):
    if symbol == ")":
        return 1
    elif symbol == "]":
        return 2
    elif symbol == "}":
        return 3
    elif symbol == ">":
        return 4
    

#get file data
file = open("advent10a.txt", "r")
fileChunks = file.readlines()

#override file data with example data
#fileChunks = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","{([(<{}[<>[]}>{[]{[(<()>","(((({<>}<{<{<>}{[]{[]{}","[[<[([]))<([[{}[[()]]]","[{[{({}]{}}([{[{{{}}([]","{<[[]]>}<{[{[{[]{()[[[]","[<(<(<(<{}))><([]([]()","<{([([[(<>()){}]>(<<{{","<{([{{}}[<[[[<>{}]]]>[]]"]
  
#get start time
start=time.time() 

opening=["(","[","{","<"]
closing=[")","]","}",">"]
finalScores=[]
for line in fileChunks:
    stack = Stack()
    corruptedScore=0
    for x in line.strip():
        #if opening a new chunk, add to stack
        if x in opening:
            stack.add(x)
        else:
            chunkOpen = stack.peek()
            
            #match opening and closing indices
            if opening.index(chunkOpen) != closing.index(x):
                corruptedScore=scoreCorruptCharacter(x)
                break
            else:
                stack.remove()
                
    #after each non-corrupted line, complete the line
    if corruptedScore == 0:
        autoCompleteScore=0
        while stack.length() != 0:
            autoCompleteScore*=5
            autoCompleteScore+=scoreAutoCompleteCharacter(closing[opening.index(stack.remove())])
        
        finalScores.append(autoCompleteScore)
  
finalScores.sort()
middleScore = median(finalScores)
                                 
#get end time 
end=time.time()
 
print("Final Score: " + str(middleScore))
print("This took " + str(end-start) + " seconds")   
        
    
