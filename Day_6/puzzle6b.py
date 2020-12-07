# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

infile = open("input.txt","r")
aa={}
total=0
people=0

for line in infile:
    line=line.rstrip()
    if line == "":
        count=0
        for key in aa.keys():
            if aa[key]==people:
                count=count+1
        total=total+count
        aa={}
        people=0
    else:
        people=people+1
        for c in line:
            if c in aa:
                aa[c]=aa[c]+1
            else:
                aa[c]=1

infile.close()
count=0
for key in aa:
    if aa[key]==people:
        count=count+1
total=total+count
print(total)
