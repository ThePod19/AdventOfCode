import time
import pathlib

def DoWork(data):
    answer = 0

    possibilities = {
        "A X": 1+3, #Rock Rock
        "A Y": 2+6, #Rock Paper
        "A Z": 3+0, #Rock Scissors
        "B X": 1+0, #Paper Rock
        "B Y": 2+3, #Paper Paper
        "B Z": 3+6, #Paper Scissors
        "C X": 1+6, #Scissors Rock
        "C Y": 2+0, #Scissors Paper
        "C Z": 3+3, #Scissors Scissors
    }

    for d in data:
        d = d.replace("\n","")
        answer += possibilities[d]

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
    if debug:
        finalData = []
    else:
        filePath = pathlib.Path(__file__).parent.resolve()
        day = str(filePath)[-1]
        file = open(f"{str(filePath)}\Advent{day}.txt", "r")
        finalData = file.readlines()
 
    return finalData
          
if __name__ == '__main__':
    main(False)
