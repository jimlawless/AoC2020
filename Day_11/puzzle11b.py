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

def lineLook(floor,x,y,xinc,yinc):
    while True:
        x=x+xinc
        y=y+yinc
        if (x<0)or(x>=len(floor[0])or(y<0)or(y>=len(floor))):
            return 0
        if floor[y][x]=="L":
            return 0
        if floor[y][x]=="#":
            return 1

def lookAround(floor,x,y):
    count=0
    count=count+lineLook(floor,x,y,-1,-1);
    count=count+lineLook(floor,x,y,0,-1);
    count=count+lineLook(floor,x,y,1,-1);
    count=count+lineLook(floor,x,y,1,0);
    count=count+lineLook(floor,x,y,1,1);
    count=count+lineLook(floor,x,y,0,1);
    count=count+lineLook(floor,x,y,-1,1);
    count=count+lineLook(floor,x,y,-1,0);
    return count



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
            howMany=lookAround(floor,x,y)
            spot=floor[y][x]
            if spot == "L":
                if howMany==0:
                    floorCopy[y][x]="#"
                    swaps=True

            if spot == "#":
                if howMany>=5:
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
