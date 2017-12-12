

with open("day11.input") as f:
    steps = f.read().split(",")

n_todir = {0: "n", 1: "ne", 2: "se", 3: "s", 4: "sw", 5: "nw"}
ndirs = len(n_todir)
dir_ton = dict([(v, k) for k, v in n_todir.iteritems()])
max_steps = 0

counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for d in steps:
    nd = dir_ton[d]
    opposite = (nd + 3) % ndirs
    op_left = (opposite - 1) % ndirs
    op_right = (opposite + 1) % ndirs

    if counts[opposite] >= 1:
        counts[opposite] -= 1
    elif counts[op_left] >= 1:
        counts[op_left] -= 1
        counts[(nd + 1) % ndirs] += 1
    elif counts[op_right] >= 1:
        counts[op_right] -= 1
        counts[(nd - 1) % ndirs] += 1
    else:
        counts[nd] += 1

    steps = sum(counts.values())
    if steps > max_steps:
        max_steps = steps

print sum(counts.values())
print max_steps
