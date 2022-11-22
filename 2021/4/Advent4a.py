#!/usr/bin/env python3

def checkColumn(card, col):
    for row in card:
        if row[col] != "X":
            return "false";
            
    return "true";
    
def checkRow(row):
    for column in row:
        if column != "X":
            return "false";
            
    return "true";    

file = open("advent4a.txt", "r")
numbers = file.readline()
calledNumbers = numbers.split(",")

bingoFile = file.readlines()
    
bingoCards=[]
counter=1
while counter < len(bingoFile):
    topLine = bingoFile[counter]

    if topLine.strip() == "":
        counter+=1
        continue
    
    bingoCards.append((bingoFile[counter].strip().replace("  "," ").split(" "),
        bingoFile[counter+1].strip().replace("  "," ").split(" "),
        bingoFile[counter+2].strip().replace("  "," ").split(" "),
        bingoFile[counter+3].strip().replace("  "," ").split(" "),
        bingoFile[counter+4].strip().replace("  "," ").split(" ")))
    
    counter+=6

print(len(bingoCards))
#print(bingoCards[0][1][2])

winningCard = 0
winningNumber = 0
for number in calledNumbers:
    for card in bingoCards:       
        for row in card:
            for column in row:
            
                columnBingo = ""
                if column != "X":
                    index = row.index(column)
                    if int(column) == int(number):
                        row[index] = "X"
                
                        columnBingo = checkColumn(card, index)    
                    
                if columnBingo == "false":
                    rowBingo = checkRow(row)
                if columnBingo == "true" or rowBingo == "true":
                    break
            if columnBingo == "true" or rowBingo == "true":
                    break

        if columnBingo == "true" or rowBingo == "true":
            winningCard = bingoCards.index(card)
            winningNumber = number
            break
    
    if winningNumber != 0:
        break

print("WinningNumber: " + str(winningNumber))
print(bingoCards[winningCard]) 
   
winningTotal = 0
for row in bingoCards[winningCard]:
    for column in row:
        if column != "X":
            winningTotal+=int(column)
            
print("Result: " + str(int(winningTotal) * int(winningNumber)))
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
