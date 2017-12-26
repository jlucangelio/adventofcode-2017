LONGEST_LEN = 0
STRONGEST = 0

def max_strength(bridge, available_components):
    results = []
    if len(bridge) == 0:
        for i, c in enumerate(available_components):
            if c[0] == 0:
                bridge.append(c)
                c = available_components.pop(i)
                r = max_strength(bridge, available_components)
                results.append(r)
                bridge.pop()
                available_components.insert(i, c)
    else:
        last = bridge[-1]
        for i, c in enumerate(available_components):
            to_append = None
            if last[1] == c[0]:
                to_append = (c[0], c[1])
            elif last[1] == c[1]:
                to_append = (c[1], c[0])

            if to_append is not None:
                bridge.append(to_append)
                c = available_components.pop(i)
                r = max_strength(bridge, available_components)
                results.append(r)
                bridge.pop()
                available_components.insert(i, c)

    if len(results) == 0:
        # No possible extensions.
        if len(bridge) > 56:
            print "error"
        length = len(bridge)
        strength = sum([p + q for (p, q) in bridge])
        return (length, strength)
        # if strength > MAX:
        #     MAX = strength
        #     MAX_BRIDGE = bridge[:]
    else:
        max_l = 0
        max_s = 0
        for l, s in results:
            if l > max_l:
                max_l = l
                max_s = s
            elif l == max_l:
                if s > max_s:
                    max_s = s

        return (max_l, max_s)


COMPONENTS = []

with open("day24.input") as f:
# with open("day24.short.input") as f:
    for line in f:
        c = tuple([int(p) for p in line.strip().split('/')])
        COMPONENTS.append(c)

print max_strength([], COMPONENTS)
# print MAX_BRIDGE, MAX