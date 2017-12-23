import math

# set b 57
# set c b
# jnz a 2
# jnz 1 5
# mul b 100
# sub b -100000
# set c b
# sub c -17000

a = 1
b = 105700
c = 122700
d = 0
e = 0
f = 0
g = 0
h = 0

print (c - b) / 17
print

for n in range(b, c + 1, 17):
    print n
    sqrt_ceil = int(math.ceil(math.sqrt(b)))
    for d in range(2, sqrt_ceil):
        if b % d == 0:
            h += 1
            break

    b += 17

print h
