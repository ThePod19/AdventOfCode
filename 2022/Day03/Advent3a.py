import time
import pathlib

def DoWork(data):
    answer = 0

    for d in data:
        d = d.replace("\n","")

        if d == "":
            continue
        
        half = int(len(d)/2)
        c1 = d[:half]
        c2 = d[half:]
        same = [c for c in c1 if c in c2]

        if same is None or len(same) == 0:
            print(d)
            print("c1",c1)
            print("c2",c2)
            
        if same[0].islower():
            answer += ord(same[0]) - 96
        else:
            answer += ord(same[0]) - 38

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
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
    else:
        filePath = pathlib.Path(__file__).parent.resolve()
        day = str(filePath)[-1]
        file = open(f"{str(filePath)}\Advent{day}.txt", "r")
        finalData = file.readlines()
 
    return finalData
          
if __name__ == '__main__':
    #print(ord("a"))
    #print(ord("b"))
    main(False)
