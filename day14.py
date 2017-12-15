INPUT = "vbqugkhl"

nset = {
    "0": 0, # 0000
    "1": 1, # 0001
    "2": 1, # 0010
    "3": 2, # 0011
    "4": 1, # 0100
    "5": 2, # 0101
    "6": 2, # 0110
    "7": 3, # 0111
    "8": 1, # 1000
    "9": 2, # 1001
    "a": 2, # 1010
    "b": 3, # 1011
    "c": 2, # 1100
    "d": 3, # 1101
    "e": 3, # 1110
    "f": 4  # 1111
}

bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"
}


def one_round(l, lengths, cur, skip):
    cur = cur
    skip = skip
    res = l[:]

    for length in lengths:
        if length == 1:
            cur += length
            cur += skip
            cur = cur % len(l)
            skip += 1
            continue

        if cur + length <= len(l):
            l = l[:cur] + list(reversed(l[cur:cur + length])) + l[cur + length:]
        else:
            prefix_len = (cur + length) - len(l)
            to_reverse = l[cur:] + l[:prefix_len]
            to_reverse.reverse()
            prefix = to_reverse[-prefix_len:]
            suffix = to_reverse[:-prefix_len]
            l = prefix + l[prefix_len:cur] + suffix

        cur += length
        cur += skip
        cur = cur % len(l)
        skip += 1

    return l, cur, skip


def knot_hash(s):
    l = range(256)
    lengths = [ord(c) for c in s]
    lengths.extend([17, 31, 73, 47, 23])

    cur = 0
    skip = 0
    for i in range(64):
        l, cur, skip = one_round(l, lengths, cur, skip)

    h = []
    for i in range(16):
        v = l[16*i]
        for j in range(1, 16):
            v = v^l[16*i+j]

        h.append(v)

    hexstr = "".join("%02x" % n for n in h)
    return hexstr

grid = [[False for _ in range(128)] for _ in range(128)]
count = 0
for i in range(128):
    s = "-".join([INPUT, str(i)])
    h = knot_hash(s)
    for j, c in enumerate(h):
        count += nset[c]

        for k, bit in enumerate(bits[c]):
            grid[i][4*j+k] = bit == "1"

print count

def used_or_not(sq):
    if sq == True:
        return "#"
    else:
        return "."

print "\n".join(["".join([used_or_not(e) for e in grid[i]]) for i in range(128)])

reached = []
visited = set()
ngroups = 0

for i in range(128):
    for j in range(128):
        if grid[i][j] == False:
            continue

        if (i, j) in visited:
            continue

        reached.append((i, j))
        ngroups += 1

        while len(reached) > 0:
            square = reached.pop(0)
            visited.add(square)

            square_x, square_y = square

            if square_x > 0 and grid[square_x - 1][square_y] == True:
                left = (square_x - 1, square_y)
                if left not in visited:
                    reached.append(left)

            if square_x < 127 and grid[square_x + 1][square_y] == True:
                right = (square_x + 1, square_y)
                if right not in visited:
                    reached.append(right)

            if square_y > 0 and grid[square_x][square_y - 1] == True:
                up = (square_x, square_y - 1)
                if up not in visited:
                    reached.append(up)

            if square_y < 127 and grid[square_x][square_y + 1] == True:
                down = (square_x, square_y + 1)
                if down not in visited:
                    reached.append(down)

print len(visited) == count
print ngroups
