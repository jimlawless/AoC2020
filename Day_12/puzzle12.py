# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

x=0
y=0
# treat N,W as -1, S,W as +1.
# NESW
directions=[-1,1,1,-1]
# begin with East
direction=1

infile = open("input.txt","r")

for line in infile:
    line=line.rstrip()
    cmd=line[0:1]
    arg=int(line[1:])
    if cmd=="F":
        if((direction==0)or(direction==2)):
            y=y+directions[direction]*arg
        else:
            x=x+directions[direction]*arg
    if cmd=="N":
        y=y+directions[0]*arg

    if cmd=="E":
        x=x+directions[1]*arg

    if cmd=="W":
        x=x+directions[3]*arg

    if cmd=="S":
        y=y+directions[2]*arg
    
    if cmd=="R":
        count=arg//90
        direction=(direction+count)% len(directions)

    if cmd=="L":
        count=arg//90
        while count>0:
            direction=direction-1
            if direction<0:
                direction = 3
            count=count -1   
infile.close()
     
print("{} {}".format(x,y))
if x<0:
    x=x*-1

if y<0:
    y=y*-1

print(x+y)
        
