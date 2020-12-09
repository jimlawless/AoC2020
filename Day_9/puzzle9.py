# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

def checkNums(start,length,val,partOne):
    global nums
    for k in range(start,length):
        if(k==partOne):
            continue
        if ((nums[k]+nums[partOne])==val):  
            print("{} + {} = {}".format(nums[k],nums[partOne],val))
            return True
    return False

nums=[]

infile = open("input.txt","r")

for line in infile:
    line=line.rstrip()
    nums.append(int(line))
infile.close()

consider=25

for i in range(consider,len(nums)):
    num=nums[i]
    found=False
    for j in range(i-consider,i):
        res=checkNums(i-consider,i,num,j)
        if res:
            found=True
            break
    if not found:
        print("Sum not found for {}".format(num))
        exit(0)
   