#!/usr/bin/env python3

import time
  
class Stack:
    def __init__(self):
        self.stack = []
      
    def add(self, data):
        self.stack.append(data)
        
    def peek(self):
        return self.stack[-1]
        
    def remove(self):
        self.stack.pop()
        
    def printStack(self):
        stackString=""
        for y in self.stack:
            stackString+=y
            
        print(stackString)
        
def score(symbol):
    if symbol == ")":
        return 3
    elif symbol == "]":
        return 57
    elif symbol == "}":
        return 1197
    elif symbol == ">":
        return 25137
    

#get file data
file = open("advent10a.txt", "r")
fileChunks = file.readlines()

#override file data with example data
#fileChunks = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","{([(<{}[<>[]}>{[]{[(<()>","(((({<>}<{<{<>}{[]{[]{}","[[<[([]))<([[{}[[()]]]","[{[{({}]{}}([{[{{{}}([]","{<[[]]>}<{[{[{[]{()[[[]","[<(<(<(<{}))><([]([]()","<{([([[(<>()){}]>(<<{{","<{([{{}}[<[[[<>{}]]]>[]]"]
  
#get start time
start=time.time() 

opening=["(","[","{","<"]
closing=[")","]","}",">"]
finalScore=0
for line in fileChunks:
    stack = Stack()
    for x in line.strip():
        #if opening a new chunk, add to stack
        if x in opening:
            stack.add(x)
        else:
            chunkOpen = stack.peek()
            
            #match opening and closing indices
            if opening.index(chunkOpen) != closing.index(x):
                finalScore+=score(x)
                break
            else:
                stack.remove()
                
        #stack.printStack()
                                 
 
#get end time 
end=time.time()
 
print("Final Score: " + str(finalScore))
print("This took " + str(end-start) + " seconds")   
        
    
