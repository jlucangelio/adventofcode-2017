layer_ranges = {}
last_layer = 0

with open("day13.input") as f:
    for line in f:
        l, r = line.strip().split(":")
        l = int(l)
        r = int(r)
        layer_ranges[l] = r
        last_layer = l

print layer_ranges

delay = 0
while True:
    if delay % 10000 == 0:
        print "delay", delay

    caught = False
    penalty = 0
    for layer in range(last_layer + 1):
        if layer not in layer_ranges:
            continue

        if (delay + layer) % ((layer_ranges[layer] - 1) * 2) == 0:
            caught = True
            penalty += layer * layer_ranges[layer]

        if delay > 0 and penalty > 0 or delay > 0 and caught:
            break

    if delay == 0:
        print "penalty", penalty

    if caught:
        delay += 1
    else:
        print "not caught", delay
        break
