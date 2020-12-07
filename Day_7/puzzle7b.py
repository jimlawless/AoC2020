# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

bagContains={}
infile = open("input.txt","r")

def countAllBags(whichBag,quantity):
    global bagContains
    s=bagContains[whichBag]
    count = quantity
    while True:
        endOfToken=s.find(" ")
        howMany=s[0:endOfToken]
        if howMany == "no":
            return quantity
        s=s[endOfToken+1:]
        endOfToken=s.find(" bag")
        newBag=s[0:endOfToken]
        count = count +countAllBags(newBag,int(howMany)*quantity)
        pos=s.find(",")
        if pos==-1:
            return count
        s=s[pos+2:]  

for line in infile:
    line=line.rstrip()
    pos=line.find(" bags contain ")
    bag=line[0:pos]
    bagContains[bag]=line[pos+len(" bags contain "):]
infile.close()

print(countAllBags("shiny gold",1)-1)