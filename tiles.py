


def findOutWhereHeCanGo(xCoordinates, yCoordinates, direction):
    if (checkIfValidDirection(xCoordinates, yCoordinates, direction) == True):
        #Do some stuff
        if (direction == 'n'):
            yCoordinates = yCoordinates - 1
        return xCoordinates, yCoordinates
    else:
        return xCoordinates, yCoordinates

def checkIfValidDirection(xCoordinates, yCoordinates, direction):
    #All the if statements to check if it is a valid direction, 9 in total


    return True

def checkIfValidLetter(letter):
    letter = letter.toLower()
    if (letter == 'n' or letter == 's' or letter == 'e' or letter == 'w'):
        return True
    else:
        print('Not a valid direction')
        return False


x = 1
y = 1
while True:
    if (x == 3 and y == 3):
        print('Victory')
        break
    direction = input("Input a direction: ")
    if (checkIfValidLetter(direction) == True):
        x, y = findOutWhereHeCanGo(x, y, direction)

    





