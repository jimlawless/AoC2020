# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

nums=[]
ones=0
threes=0

infile = open("input.txt","r")

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

for i in range(1,len(nums)):
    diff=nums[i]-nums[i-1]
    if diff==3:
        threes=threes+1
    if diff==1:
        ones=ones+1

print("Ones: {}   Threes: {}".format(ones,threes))

print("Product is {}".format(ones*threes))
