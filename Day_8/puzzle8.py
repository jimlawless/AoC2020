# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

instructions=[]

accum=0
ip=0

infile = open("input.txt","r")

for line in infile:
    line=line.rstrip()
    instructions.append(line)
infile.close()

while True:
    ins=instructions[ip]
    if ins[0:3]=="nop":
        instructions[ip]="end"
        ip=ip+1
        continue
    if ins[0:3]=="jmp":
        instructions[ip]="end"
        arg=int(ins[4:].rstrip())
        ip=ip+arg
        continue
    if ins[0:3]=="acc":
        instructions[ip]="end"
        arg=int(ins[4:].rstrip())
        accum=accum+arg
        ip=ip+1
        continue
    if ins[0:3]=="end":
        break
print(accum)

        
    
        