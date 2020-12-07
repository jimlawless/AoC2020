
infile = open("input.txt","r")
aa={}
total=0
for line in infile:
    line=line.rstrip()
    if line == "":
        count=0
        for ct in aa:
            count=count+1
        total=total+count
        aa={}
    else:
        for c in line:
            aa[c]=1

infile.close()
count=0
for ct in aa:
    count=count+1
total=total+count
print(total)






