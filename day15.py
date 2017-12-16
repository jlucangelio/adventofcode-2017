GA = 591
GB = 393

def gen_a1():
    n = GA

    while True:
        n = n * 16807
        n = n % 2147483647
        yield n


def gen_b1():
    n = GB

    while True:
        n = n * 48271
        n = n % 2147483647
        yield n


def gen_a2():
    n = GA

    while True:
        n = n * 16807
        n = n % 2147483647
        if n % 4 == 0:
            yield n


def gen_b2():
    n = GB

    while True:
        n = n * 48271
        n = n % 2147483647
        if n % 8 == 0:
            yield n


a = gen_a2()
b = gen_b2()
count = 0
for i in range(5000000):
    if i % 10000 == 0:
        print i

    na = next(a)
    nb = next(b)

    hex_a = str(hex(na))
    hex_b = str(hex(nb))

    if hex_a[-4:] == hex_b[-4:]:
        count += 1

print count
