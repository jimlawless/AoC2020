# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

# This entry did not finish and probably won't finish in the foreseeable
# future.  I have to study the solutions I found online that worked to
# understand what they did instead of my brute-force approach.
#
# (It works fine for the two smaller examples. ;-)
nums=[]

count=0

infile = open("input.txt","r")

def scanList(n,ndx,sofar):
    global count
    if(n[ndx]==highest):
        #print(sofar)
        count=count+1
        if((count%131072)==0):
            print(count,end="\r")
        return
    if ndx<(len(n)-1):
        if (n[ndx+1]-n[ndx])<4:
            scanList(n,ndx+1,sofar+","+str(n[ndx+1]))
        else:
            return
    else:   
        return
    if ndx<len(n)-2:
        if (n[ndx+2]-n[ndx])<4:
            scanList(n,ndx+2,sofar+","+str(n[ndx+2]))
        else:
            return
    else:
        return
    if ndx<len(n)-3:
        if (n[ndx+3]-n[ndx])<4:
            scanList(n,ndx+3,sofar+","+str(n[ndx+3]))


for line in infile:
    line=line.rstrip()
    nums.append(int(line))
infile.close()

highest=0
for num in nums:
    if num > highest:
        highest = num
highest=highest+3
print("highest {} ".format(highest))
nums.insert(0,0)
nums.append(highest)
nums.sort()
count=0
scanList(nums,0,"0")
print("\nTotal # of combinations: {}".format(count))
