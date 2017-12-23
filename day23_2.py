import time

INSTRUCTIONS = []

with open("day23.input") as f:
    for line in f.readlines():
        tokens = line.strip().split()
        op = tokens[0]

        dst = tokens[1]
        src = None
        if len(tokens) > 2:
            src = tokens[2]

        INSTRUCTIONS.append((op, dst, src))

# print INSTRUCTIONS

regs = {
    'a': 1,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
}

def get_operand(operand):
    if operand in regs:
        return regs[operand]
    else:
        return int(operand)

pc = 0
mul_count = 0
its = 0
while pc >= 0 and pc < len(INSTRUCTIONS):
    its += 1
    if its % 1000000 == 0:
        print pc
        print regs
        time.sleep(2)

    op, dst, src = INSTRUCTIONS[pc]

    if op == "set":
        regs[dst] = get_operand(src)
    if op == "inc":
        regs[dst] += 1
    elif op == "sub":
        regs[dst] -= get_operand(src)
        if dst == 'h':
            print regs

    elif op == "mul":
        regs[dst] = regs[dst] * get_operand(src)
        # mul_count += 1
    elif op == "jnz":
        if get_operand(dst) != 0:
            pc += get_operand(src)
        else:
            pc += 1

    if op != "jnz":
        pc += 1

    print pc
    print regs
    time.sleep(2)

# print mul_count
print regs['h']
