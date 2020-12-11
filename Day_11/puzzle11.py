# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

floor=[]
swaps=True

def printFloor():
    global floor
    for line in floor:
        for c in line:
            print(c,end="")
        print("")
    print("")

def getAdjacent(floor,x,y):
    if (x>=0)and(x<len(floor[0])):
        if(y>=0)and(y<len(floor)):
            return floor[y][x]
    return ""

def computeAdjacent(floor,x,y):
    adjacent=[]
    # get values for x-1,y x-1,y+1 x,y+1 x+1,y+1 x+1,y x+1,y-1 x,y-1 x-1,y-1
    adjacent.append(getAdjacent(floor,x-1,y))
    adjacent.append(getAdjacent(floor,x-1,y+1))
    adjacent.append(getAdjacent(floor,x,y+1))
    adjacent.append(getAdjacent(floor,x+1,y+1))
    adjacent.append(getAdjacent(floor,x+1,y))
    adjacent.append(getAdjacent(floor,x+1,y-1))
    adjacent.append(getAdjacent(floor,x,y-1))
    adjacent.append(getAdjacent(floor,x-1,y-1))
    return adjacent

infile = open("input.txt","r")


for line in infile:
    line=line.rstrip()
    floor.append(list(line))
infile.close()

printFloor()

def processRound(floor):
    global swaps
    floorCopy=[]
    for f in floor:
        floorCopy.append(f.copy())

    swaps=False

    for y in range(0,len(floor)):
        for x in range(0,len(floor[y])):
            adjacent=computeAdjacent(floor,x,y)
            spot=floor[y][x]
            if spot == "L":
                occ=False
                for i in adjacent:
                    if i=="#":
                        occ=True
                if not occ:
                    floorCopy[y][x]="#"
                    swaps=True
            if spot == "#":
                occCount=0
                for i in adjacent:
                    if i=="#":
                        occCount=occCount+1
                if occCount>=4:
                    floorCopy[y][x]="L"
                    swaps=True
    return floorCopy

while swaps:
    floor=processRound(floor)
    printFloor()        

count=0
for row in floor:
    for column in row:
        if column == "#":
            count=count+1
print(count)
