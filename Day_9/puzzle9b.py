# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE


nums=[]
needle=15690279

infile = open("input.txt","r")

def searchArray(start):
    global nums
    sum=0
    largest=nums[start]
    smallest=nums[start]
    for j in range(start,len(nums)):
        if nums[j]<smallest:
            smallest=nums[j]
        if nums[j]>largest:
            largest=nums[j]
        sum=sum+nums[j]
        if sum==needle:
            print("{} {} {}".format(smallest,largest,smallest+largest))
            exit(0)

for line in infile:
    line=line.rstrip()
    nums.append(int(line))
infile.close()

for i in range(0,len(nums)):
    searchArray(i)
