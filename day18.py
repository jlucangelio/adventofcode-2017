from collections import defaultdict

INSTRUCTIONS = []

with open("day18.input") as f:
    INSTRUCTIONS = [line.strip() for line in f.readlines()]

# print INSTRUCTIONS

regs = defaultdict(lambda: 0)

pc = 0
sent = None
received = None
while pc < len(INSTRUCTIONS):
    print regs
    ins = INSTRUCTIONS[pc]
    tokens = ins.split()
    op = tokens[0]

    dst = tokens[1]
    src = None
    src_is_reg = False
    if len(tokens) > 2:
        src = tokens[2]

        if len(src) == 1 and ord(src) >= ord('a') and ord(src) <= 'z':
            src_is_reg = True
            src = regs[src]
        else:
            src = int(src)

    if op == "snd":
        sent = regs[dst]
    elif op == "set":
        regs[dst] = src
    elif op == "add":
        regs[dst] += src
    elif op == "mul":
        regs[dst] = regs[dst] * src
    elif op == "mod":
        regs[dst] = regs[dst] % src
    elif op == "rcv":
        if regs[dst] != 0:
            received = sent
            print received
            break
    elif op == "jgz":
        if regs[dst] > 0:
            pc += src
        else:
            pc += 1

    if op != "jgz":
        pc += 1

