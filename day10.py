SINPUT = "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243"
INPUT = [int(e) for e in SINPUT.split(',')]
SIZE = 256

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


l = range(SIZE)
l, _, _ = one_round(l, INPUT, 0, 0)

print l[0] * l[1]
print

l = range(SIZE)
lengths = [ord(c) for c in SINPUT]
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

print h
hexstr = "".join("%02x" % n for n in h)
print hexstr, len(hexstr)
