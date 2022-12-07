import time
import pathlib
import matplotlib.pyplot as plt
import numpy as np

def DoWork(data):
    answer = 0

    for d in data:
        d = d.replace("\n","")

        e1,e2 = d.split(",")
        e11,e12 = e1.split("-")
        e21,e22 = e2.split("-")

        if int(e11) <= int(e21) and int(e12) >= int(e22):
            answer += 1
        elif int(e11) >= int(e21) and int(e12) <= int(e22):
            answer += 1

    return answer

def main(arg):
    global debug
    debug = arg

    start=time.time()

    data = getData()
    
    result = DoWork(data)
            
    if debug:
        expected = 157
        print(expected)
        print(result)
        print("Success? " + str(expected == sum))
        
    end=time.time()
      
    print("Result: " + str(result))
    print("This took " + str(end-start) + " seconds")  

def getData():
    if debug:
        finalData = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
        ]
    else:
        filePath = pathlib.Path(__file__).parent.resolve()
        day = str(filePath)[-1]
        file = open(f"{str(filePath)}\Advent{day}.txt", "r")
        finalData = file.readlines()
 
    return finalData
          
if __name__ == '__main__':
    main(False)
