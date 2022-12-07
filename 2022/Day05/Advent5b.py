import time
import pathlib

def DoWork(data, stacks):
    firstMoveRow = data.index("\n") + 1

    for d in data[firstMoveRow:]:
        nums = [n for n in d.split() if n.isnumeric()]
        moves = int(nums[0])
        removing = int(nums[1])-1
        adding = int(nums[2])-1

        grabbedCrates = stacks[removing][-moves:]
        for grabbedCrate in grabbedCrates:
            stacks[adding].append(grabbedCrate)

        del stacks[removing][-moves:]

    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer

def StackCargo(data):
    stackRow = data.index("\n") - 1

    stacks = []
    for stackNum in data[stackRow]:
        if stackNum == " " or stackNum == "\n":
            continue

        stacks.append([])
        index = data[stackRow].index(stackNum)
        for crate in data[stackRow-1::-1]:
            if crate[index] == " " or stackNum == "\n":
                continue

            stacks[int(stackNum) - 1].append(crate[index])

    return stacks

def main(arg):
    global debug
    debug = arg

    start=time.time()

    data = getData()

    stacks = StackCargo(data)

    result = DoWork(data, stacks)
            
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
        finalData = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "\n",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]
    else:
        filePath = pathlib.Path(__file__).parent.resolve()
        day = str(filePath)[-1]
        file = open(f"{str(filePath)}\Advent{day}.txt", "r")
        finalData = file.readlines()
 
    return finalData
          
if __name__ == '__main__':
    main(False)
