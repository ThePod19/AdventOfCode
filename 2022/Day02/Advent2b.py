import time
import pathlib

def DoWork(data):
    answer = 0

    possibilities = {
        "A X": 0+3, #Rock Scissors
        "A Y": 3+1, #Rock Rock
        "A Z": 6+2, #Rock Paper
        "B X": 0+1, #Paper Rock
        "B Y": 3+2, #Paper Paper
        "B Z": 6+3, #Paper Scissors
        "C X": 0+2, #Scissors Paper
        "C Y": 3+3, #Scissors Scissors
        "C Z": 6+1, #Scissors Rock
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
