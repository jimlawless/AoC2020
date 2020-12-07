# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

rules=[]
used=""

def searchRules(srch):
    global rules
    global used
    count=0
    for rule in rules:
        if rule.find(srch) >= 0:
            contain=rule.find(" bags contain")
            has=rule.find(srch)
            if has > contain:
                bagtype=rule[0:contain]
                if used.find(bagtype)<0:
                    count = count + 1
                    used=used+"|"+bagtype   
                    count=count+searchRules(bagtype)
    return count

infile = open("input.txt","r")
total=0
for line in infile:
    line=line.rstrip()
    rules.insert(0,line)
infile.close()

print(searchRules("shiny gold"))
