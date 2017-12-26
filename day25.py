from collections import defaultdict, namedtuple

Action = namedtuple("Action", "write move next_state")
State = namedtuple("State", "name actions")

with open("day25.input") as f:
    LINES = [line.strip() for line in f.readlines()]

start = None
states = {}

skip = 0
steps = 0
for i in range(len(LINES)):
    if skip > 0:
        skip -= 1
        continue

    line = LINES[i]

    if len(line) == 0:
        continue

    if "Begin" in line:
        start = line.split()[3][0]
        print "start", start

    if "Perform" in line:
        steps = int(line.split()[5])
        print "steps", steps

    if "In state" in line:
        # In state A:
        #   If the current value is 0:
        #     - Write the value 1.
        #     - Move one slot to the right.
        #     - Continue with state B.
        #   If the current value is 1:
        #     - Write the value 0.
        #     - Move one slot to the left.
        #     - Continue with state E.
        name = line.split()[2][:-1]
        print "name", name
        # zero
        w0 = int(LINES[i+2].split()[4][0])
        d = LINES[i+3].split()[6][:-1]
        if d == "left":
            m0 = -1
        elif d == "right":
            m0 = 1
        s0 = LINES[i+4].split()[4][0]
        # one
        w1 = int(LINES[i+6].split()[4][0])
        d = LINES[i+7].split()[6][:-1]
        if d == "left":
            m1 = -1
        elif d == "right":
            m1 = 1
        s1 = LINES[i+8].split()[4][0]
        states[name] = State(name, [Action(w0, m0, s0), Action(w1, m1, s1)])
        skip = 8

tape = defaultdict(int)
cur_state = start
cur_pos = 0

for i in range(steps):
    tape_value = int(tape[cur_pos])
    st = states[cur_state]
    action = st.actions[tape_value]

    tape[cur_pos] = action.write
    cur_pos += action.move
    cur_state = action.next_state

count = 0
for k in tape:
    if tape[k] == 1:
        count += 1

print "done"
print count
