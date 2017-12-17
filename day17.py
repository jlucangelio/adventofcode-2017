INPUT = 345
# INPUT = 3

buf = [0]
pos = 0
for i in range(1, 2018):
    if i % 10000 == 0:
        print i
    pos = (pos + INPUT) % i
    prefix = buf[:(pos + 1)]
    prefix.append(i)
    prefix.extend(buf[pos + 1:])
    buf = prefix
    # buf = buf[:(pos + 1)] + [i] + buf[pos + 1:]
    pos = pos + 1
    print buf[buf.index(0) + 1]

print buf[buf.index(2017) + 1]

pos = 0
after_zero = None
for i in range(1, 50000000):
    if i % 10000 == 0:
        print i
    pos = (pos + INPUT) % i
    if pos == 0:
        after_zero = i
        print after_zero
    pos = pos + 1

print after_zero
