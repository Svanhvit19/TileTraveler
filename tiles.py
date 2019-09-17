#start
x = 1
y = 1
#input

#move
def north(x,y):
    y += 1
    return (x,y)

def south(x,y):
    y -= 1
    return x,y

def east(x,y):
    x += 1
    return (x,y)

def west(x,y):
    x -= 1
    return x,y

direction = input("Direction: ")
#while 0 < x <= 3 and 0 < y <= 3:
if direction == "N" or "n":
    place = north(x,y)
    print(place)
elif direction == "S" or "s":
    place = south(x,y)
    print(place)
elif direction == "E" or "e":
    place = east(x,y)
    print(place)
elif direction == "W" or "w":
    place = west(x,y)
    print(place)
else:
    print("Not a valid direction")
    #direction = input("Direction: ")