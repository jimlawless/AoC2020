
def seatNum(bpass):
    lo=0
    hi=127
    fb=bpass[0:7]
    for c in fb:
        if c=="F":
            hi=(lo+hi)//2
        else:
            lo=(lo+hi+1)//2
    
    row = (lo+hi)//2

    lo=0
    hi=7
    lr=bpass[7:10]
    for c in lr:
        if c=="L":
            hi=(lo+hi)//2
        else:
            lo=(lo+hi+1)//2
    col=(lo+hi)//2
    seat = row * 8 + col
    #print("{0} {1} {2}".format(row,col,seat))
    return seat

print(seatNum("BFFFBBFRRR"))
print(seatNum("FFFBBBFRRR"))
print(seatNum("BBFFBBFRLL"))

biggest=0
seats=[]
for i in range(128*8):
    seats.insert(i,0)

infile = open("input.txt","r")
for line in infile:
    s=seatNum(line)
    seats[s]=s
    if(s>biggest):
        biggest=s
infile.close()

print("Biggest is {}".format(biggest))

for i in range(biggest):
    if(seats[i]==0):
        print(i)



