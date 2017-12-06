import math
import sys

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...


INPUT = 23
INPUT = 325489
INPUT = int(sys.argv[1])

side_len = int(math.ceil(math.sqrt(INPUT)))

if side_len % 2 == 0:
    side_len += 1
print "side_len", side_len

ring = (side_len - 1)/2
print "ring", ring

first_value_in_ring = (2 * ring - 1)**2 + 1

print "first_value", first_value_in_ring

index = INPUT - first_value_in_ring

print "index", index

offset = index % (side_len - 1)

distance = ring + int(math.fabs(-(ring - 1) + offset))

print distance
