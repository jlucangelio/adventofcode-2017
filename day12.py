with open("day12.input") as f:
    pipes = f.readlines()

programs = {}
for pipe in pipes:
    # 1999 <-> 964, 1568
    program, pipes_to = pipe.split(" <-> ")
    pipes_to = [int(tok) for tok in pipes_to.split(", ")]
    programs[int(program)] = pipes_to

print len(programs)

reached = [0]
visited = set()
groups = []

for i in range(len(programs)):
    if i not in visited:
        reached.append(i)
        groups.append(i)

        while True:
            n = reached.pop(0)
            visited.add(n)
            for p in programs[n]:
                if p not in visited:
                    reached.append(p)

            if len(reached) == 0:
                break

        print len(visited)

print len(groups)
