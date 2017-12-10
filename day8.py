class RegisterBank(object):
    def __init__(self):
        self.regs = {}

    def get(self, reg):
        if reg in self.regs:
            return self.regs[reg]
        else:
            self.regs[reg] = 0
            return 0

    def set(self, reg, val):
        self.regs[reg] = val


with open("day8.input") as f:
    instrs = f.readlines()

rb = RegisterBank()
max_val = 0
for instr in instrs:
    # koq inc 675 if xrh >= -6

    dest_reg, op, val, _, cond_reg, comp_op, comp_arg = instr.strip().split()

    proceed = False
    if comp_op == "<":
        comp = lambda x, y: x < y
    elif comp_op == "<=":
        comp = lambda x, y: x <= y
    elif comp_op == ">":
        comp = lambda x, y: x > y
    elif comp_op == ">=":
        comp = lambda x, y: x >= y
    elif comp_op == "==":
        comp = lambda x, y: x == y
    elif comp_op == "!=":
        comp = lambda x, y: x != y

    proceed = comp(rb.get(cond_reg), int(comp_arg))

    if proceed:
        new_val = rb.get(dest_reg)
        if op == "inc":
            print "inc"
            new_val += int(val)
        elif op == "dec":
            print "dec"
            new_val -= int(val)

        rb.set(dest_reg, new_val)

    max_val = max(max_val, max(rb.regs.values()))

print max(rb.regs.values())
print max_val
