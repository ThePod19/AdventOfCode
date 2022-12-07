import time
import pathlib

def DoWork(data):
    data = data[0]
    answer = 14

    start = 0
    while True:
        buffer = data[start:start+14]

        if len(set(buffer)) == 14:
            break
        else:
            answer += 1
            start += 1

    return answer

def main(arg):
    global debug
    debug = arg

    start=time.time()

    data = getData()

    result = DoWork(data)
            
    if debug:
        expected = "MCD"
        print("Expected:",expected)
        print("Actual:",result)
        print("Success? " + str(expected == result))
        
    end=time.time()
      
    print("Result: " + str(result))
    print("This took " + str(end-start) + " seconds")  

def getData():
    if debug:
        finalData = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]
    else:
        filePath = pathlib.Path(__file__).parent.resolve()
        day = str(filePath)[-1]
        file = open(f"{str(filePath)}\Advent{day}.txt", "r")
        finalData = file.readlines()
 
    return finalData
          
if __name__ == '__main__':
    main(False)
