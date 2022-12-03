import sys
import time
import math
import pathlib
import urllib

def DoWork(data):
    answer = 0

    elves = []
    sum = 0
    for d in data:
        if d == "\n":
            elves.append(sum)
            sum=0
        else:
            sum += int(d)

    answer = max(elves)

    return answer

def main(arg):
    global debug
    debug = arg

    start=time.time()

    data = getData()
    
    result = DoWork(data)
            
    if debug:
        expected = ""
        print(expected)
        print(result)
        print("Success? " + str(expected == sum))
        
    end=time.time()
      
    print("Result: " + str(result))
    print("This took " + str(end-start) + " seconds")  

def getData():
    if not debug:
        filePath = pathlib.Path(__file__).parent.resolve()
        day = str(filePath)[-1]
        file = open(f"{str(filePath)}\Advent{day}.txt", "r")
        fileData = file.readlines()
    
    if debug:
        fileData = []
        
    return fileData
          
if __name__ == '__main__':
    main(False)
