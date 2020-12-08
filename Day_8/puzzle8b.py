# Jim Lawless
# License: https://github.com/jimlawless/AoC2020/LICENSE

instructions=[]

infile = open("input.txt","r")

for line in infile:
    line=line.rstrip()
    instructions.append(line)
infile.close()
instructions.append("bye")
hold=instructions.copy()
last=-1

done=False
while not done:
    instructions=hold.copy()
    ip=0
    while True:
        ins=instructions[ip]
        if ins[0:3]=="jmp":
            if ip > last:
                last=ip
                instructions[ip]="nop" + ins[3:]
                break
        else:
            if ins[0:3]=="nop":
                if ip > last:
                    last=ip
                    instructions[ip]="jmp" + ins[3:]
                    break
        ip=ip+1

    accum=0
    ip=0

    while True:
        if done:
            break
        ins=instructions[ip]
        if ins[0:3]=="bye":
            print("normal termination ... accum is {}".format(accum))
            done=True
            continue
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

        
    
        