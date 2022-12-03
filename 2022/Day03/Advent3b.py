import time
import pathlib

def DoWork(data):
    answer = 0

    for d1 in data[0::3]:
        index = data.index(d1)
        d1 = d1.replace("\n","")
        d2 = data[index+1].replace("\n","")
        d3 = data[index+2].replace("\n","")

        if d1 == "" or d2 == "" or d3 == "":
            raise Exception("Elf missing from group")
        
        same = [d for d in d1 if d in d2]
        same2 = [d for d in same if d in d3]

        if same2 is None or len(same2) == 0:
            print(d)
            print("d1",d1)
            print("d2",d2)
            print("d3",d3)
            
        if same2[0].islower():
            answer += ord(same2[0]) - 96
        else:
            answer += ord(same2[0]) - 38

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
