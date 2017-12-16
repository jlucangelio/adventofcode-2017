with open("day16.input") as f:
    INPUT = f.read().strip().split(',')

ORD_A = 97

programs = [(ORD_A + i) for i in range(16)]
print programs

for i in xrange(1000):
    if i % 100 == 0:
        print i, "".join([chr(p) for p in programs])

    for move in INPUT:
        if move[0] == 'x':
            # xA/B - positions
            # print "exchange"
            pos_a, pos_b = move[1:].split('/')
            pos_a = int(pos_a)
            pos_b = int(pos_b)
            prog_at_a = programs[pos_a]
            programs[pos_a] = programs[pos_b]
            programs[pos_b] = prog_at_a
            # programs[pos_a] = programs[pos_a] ^ programs[pos_b]
            # programs[pos_b] = programs[pos_b] ^ programs[pos_a]
            # programs[pos_a] = programs[pos_a] ^ programs[pos_b]
        elif move[0] == 's':
            # print "spin"
            index = int(move[1:])
            programs = programs[-index:] + programs[:-index]
        elif move[0] == 'p':
            # pA/B - names
            # print "partner"
            name_a, name_b = move[1:].split('/')
            pos_a = programs.index(ord(name_a))
            pos_b = programs.index(ord(name_b))
            prog_at_a = programs[pos_a]
            programs[pos_a] = programs[pos_b]
            programs[pos_b] = prog_at_a
            # programs[pos_a] = programs[pos_a] ^ programs[pos_b]
            # programs[pos_b] = programs[pos_b] ^ programs[pos_a]
            # programs[pos_a] = programs[pos_a] ^ programs[pos_b]

print "".join([chr(p) for p in programs])
