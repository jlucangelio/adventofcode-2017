from collections import defaultdict

def is_letter(e):
    return ord(e) >= ord('a') and ord(e) <= 'z'

def process_src(tokens, regs):
    src = None
    if len(tokens) > 2:
        src = tokens[2]

        if len(src) == 1 and is_letter(src):
            src = regs.get(src)
        else:
            src = int(src)

    return src


INSTRUCTIONS = []

with open("day18.input") as f:
    INSTRUCTIONS = [line.strip() for line in f.readlines()]

# print INSTRUCTIONS
regs_0 = defaultdict(lambda: 0)
regs_0['p'] = 0
regs_1 = defaultdict(lambda: 0)
regs_1['p'] = 1

pc_0 = 0
pc_1 = 0

prog_0_recv = []
prog_1_recv = []

p0_blocked = False
p1_blocked = False

send_count = 0

while pc_0 < len(INSTRUCTIONS) or pc_1 < len(INSTRUCTIONS):
    # print "0", pc_0, "len", len(prog_0_recv)
    # print "1", pc_1, "len", len(prog_1_recv)

    if pc_0 < len(INSTRUCTIONS) and not p0_blocked:
        ins0 = INSTRUCTIONS[pc_0]
        tokens0 = ins0.split()
        op0 = tokens0[0]
        dst0 = tokens0[1]
        src0 = process_src(tokens0, regs_0)

        if op0 == "snd":
            prog_1_recv.append(regs_0[dst0])
            if len(prog_1_recv) == 1:
                p1_blocked = False
                # print "unblocked 1"
        elif op0 == "set":
            regs_0[dst0] = src0
        elif op0 == "add":
            regs_0[dst0] += src0
        elif op0 == "mul":
            regs_0[dst0] = regs_0[dst0] * src0
        elif op0 == "mod":
            regs_0[dst0] = regs_0[dst0] % src0
        elif op0 == "rcv":
            if len(prog_0_recv) > 0:
                regs_0[dst0] = prog_0_recv.pop(0)
            else:
                p0_blocked = True
                # print "0 is blocked"
        elif op0 == "jgz":
            if is_letter(dst0) and regs_0[dst0] > 0 or not is_letter(dst0) and int(dst0) > 0:
                pc_0 += src0
            else:
                pc_0 += 1

        if op0 != "jgz" and not p0_blocked:
            pc_0 += 1


    if pc_1 < len(INSTRUCTIONS) and not p1_blocked:
        ins1 = INSTRUCTIONS[pc_1]
        tokens1 = ins1.split()
        op1 = tokens1[0]
        dst1 = tokens1[1]
        src1 = process_src(tokens1, regs_1)

        if op1 == "snd":
            prog_0_recv.append(regs_1[dst1])
            send_count += 1
            if len(prog_0_recv) == 1:
                p0_blocked = False
                # print "unblocked 0"
        elif op1 == "set":
            regs_1[dst1] = src1
        elif op1 == "add":
            regs_1[dst1] += src1
        elif op1 == "mul":
            regs_1[dst1] = regs_1[dst1] * src1
        elif op1 == "mod":
            regs_1[dst1] = regs_1[dst1] % src1
        elif op1 == "rcv":
            if len(prog_1_recv) > 0:
                regs_1[dst1] = prog_1_recv.pop(0)
            else:
                p1_blocked = True
                # print "1 is blocked"
        elif op1 == "jgz":
            if is_letter(dst1) and regs_1[dst1] > 0 or not is_letter(dst1) and int(dst1) > 0:
                pc_1 += src1
            else:
                pc_1 += 1

        if op1 != "jgz":
            if not p1_blocked:
                pc_1 += 1

    if p0_blocked and p1_blocked:
        print "Deadlock!"
        break

print send_count
