import math
import sys

from collections import namedtuple

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

def get_side_len(num):
    ret = int(math.ceil(math.sqrt(num)))

    if ret % 2 == 0:
        ret += 1

    return ret


def get_ring_num(num):
    return (side_len - 1)/2


def get_first_value_in_ring(ring):
    return (2 * ring - 1)**2 + 1


def coords(num):
    side_len = get_side_len(INPUT)
    ring = get_ring_num(side_len)
    first_value_in_ring = get_first_value_in_ring(ring)
    index = num - first_value_in_ring
    offset = offset = index % (side_len - 1)
    coord = -(ring - 1) + offset
    side = index // (side_len - 1)

    if side == 0:
        return (ring, coord)
    elif side == 2:
        return (-ring, coord)
    elif side == 1:
        return (coord, ring)
    elif side == 3:
        return (coord, -ring)


INPUT = 23
INPUT = 325489
INPUT = int(sys.argv[1])

side_len = get_side_len(INPUT)
print "side_len", side_len

ring = get_ring_num(side_len)
print "ring", ring

first_value_in_ring = get_first_value_in_ring(ring)

print "first_value", first_value_in_ring

index = INPUT - first_value_in_ring

print "index", index

offset = index % (side_len - 1)

distance = ring + int(math.fabs(-(ring - 1) + offset))

print distance

print coords(INPUT)

Coord = namedtuple("Coord", "x y")

sums = {}

def add(c, sums):
    total = 0
    # c = Coord(cds[0], cds[1])
    left = Coord(c.x + 1, c.y)
    top = Coord(c.x, c.y + 1)
    right = Coord(c.x - 1, c.y)
    bot = Coord(c.x, c.y - 1)
    leftup = Coord(c.x + 1, c.y + 1)
    rightup = Coord(c.x - 1, c.y + 1)
    rightdown = Coord(c.x - 1, c.y - 1)
    leftdown = Coord(c.x + 1, c.y - 1)

    for c in (left, top, right, bot, leftup, rightup, rightdown, leftdown):
        if c in sums:
            total += sums[c]

    return total


def fill(num):
    c = Coord(0, 0)
    sums[c] = 1
    ring = 0

    c = Coord(1, 0)
    ring = 1
    for i in range(num-1):
        # add
        s = add(c, sums)
        if s > num:
            print s
            break

        sums[c] = s

        if c.x == ring and c.y == -ring:
            # finished ring
            ring += 1
            # move right
            c = c._replace(x=c.x + 1)
            print "new ring", ring
            continue

        if c.x == ring:
            # on the left
            if c.y == ring:
                # turn left
                c = c._replace(x=c.x - 1)
            else:
                # move up
                c = c._replace(y=c.y + 1)
        elif c.y == ring:
            # on the top
            if c.x == -ring:
                # turn down
                c = c._replace(y=c.y - 1)
            else:
                # move left
                c = c._replace(x=c.x - 1)
        elif c.x == -ring:
            # on the right
            if c.y == -ring:
                # turn right
                c = c._replace(x=c.x + 1)
            else:
                # move down
                c = c._replace(y=c.y - 1)
        elif c.y == -ring:
            # on the bottom
            if c.x == ring:
                # turn up
                c = c._replace(y=c.y + 1)
            else:
                # move left
                c = c._replace(x=c.x + 1)

fill(INPUT)
