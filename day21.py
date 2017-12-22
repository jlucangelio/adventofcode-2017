def flip_pattern_h(p):
    new_p = []
    new_p.append("".join(reversed(p[0])))
    new_p.append("".join(reversed(p[1])))
    if len(p) > 2:
        new_p.append("".join(reversed(p[2])))

    return tuple(new_p)


def flip_pattern_v(p):
    new_p = []
    if len(p) > 2:
        new_p.append(p[2])
    new_p.append(p[1])
    new_p.append(p[0])

    return tuple(new_p)


def add_flips(ip, op, rules):
    flippedh = flip_pattern_h(ip)
    if flippedh not in rules:
        rules[flippedh] = op

    flippedv = flip_pattern_v(ip)
    if flippedv not in rules3:
        rules[flippedv] = op


def rotate_pattern_clockwise_90(p):
    new_p = []

    if len(p) == 2:
        new_p.append(p[1][0] + p[0][0])
        new_p.append(p[1][1] + p[0][1])

    if len(p) == 3:
        new_p.append(p[2][0] + p[1][0] + p[0][0])
        new_p.append(p[2][1] + p[1][1] + p[0][1])
        new_p.append(p[2][2] + p[1][2] + p[0][2])

    return tuple(new_p)


def rotate_pattern_clockwise_180(p):
    return rotate_pattern_clockwise_90(rotate_pattern_clockwise_90(p))


def rotate_pattern_clockwise_270(p):
    return rotate_pattern_clockwise_180(rotate_pattern_clockwise_90(p))


def rotate_pattern_clockwise_360(p):
    return rotate_pattern_clockwise_180(rotate_pattern_clockwise_180(p))


def add_rotations(ip, op, rules):
    rotated90 = rotate_pattern_clockwise_90(ip)
    if rotated90 not in rules:
        rules[rotated90] = op
    add_flips(rotated90, op, rules)

    rotated180 = rotate_pattern_clockwise_180(ip)
    if rotated180 not in rules:
        rules[rotated180] = op
    add_flips(rotated180, op, rules)

    rotated270 = rotate_pattern_clockwise_270(ip)
    if rotated270 not in rules:
        rules[rotated270] = op
    add_flips(rotated270, op, rules)


def print_pattern(p):
    print p[0]
    print p[1]
    if len(p) > 2:
        print p[2]


rules2 = {}
rules3 = {}

image = tuple(".#./..#/###".split('/'))
print rotate_pattern_clockwise_360(image) == image

with open("day21.input") as f:
    for line in f.readlines():
        i, o = line.strip().split(" => ")

        if i.count('/') == 1:
            # 2-rule
            ipattern = tuple(i.split('/'))
            opattern = tuple(o.split('/'))

            rules2[ipattern] = opattern
            add_flips(ipattern, opattern, rules2)
            add_rotations(ipattern, opattern, rules2)

        elif i.count('/') == 2:
            # 3-rule
            ipattern = tuple(i.split('/'))
            opattern = tuple(o.split('/'))

            rules3[ipattern] = opattern
            add_flips(ipattern, opattern, rules3)
            add_rotations(ipattern, opattern, rules3)

for i in range(18):
    new_image = []
    squares = {}
    if len(image) % 2 == 0:
        squares = {}
        for j in range(len(image) / 2):
            for k in range(len(image) / 2):
                isquare = tuple([image[2*j][2*k:2*k+2],
                                 image[2*j+1][2*k:2*k+2]])
                if isquare in rules2:
                    squares[(j, k)] = rules2[isquare]
                else:
                    print "error, square not in rules"
                    print_pattern(isquare)
                    print
                    break

        for j in range(len(image) / 2):
            new_image.append("")
            new_image.append("")
            new_image.append("")
            for k in range(len(image) / 2):
                new_image[3*j] += squares[(j, k)][0]
                new_image[3*j+1] += squares[(j, k)][1]
                new_image[3*j+2] += squares[(j, k)][2]

    elif len(image) % 3 == 0:
        for j in range(len(image) / 3):
            for k in range(len(image) / 3):
                isquare = tuple([image[3*j][3*k:3*k+3],
                                 image[3*j+1][3*k:3*k+3],
                                 image[3*j+2][3*k:3*k+3]])
                if isquare in rules3:
                    squares[(j, k)] = rules3[isquare]
                else:
                    print "error, square not in rules"
                    print_pattern(isquare)
                    print
                    break

        for j in range(len(image) / 3):
            new_image.append("")
            new_image.append("")
            new_image.append("")
            new_image.append("")
            for k in range(len(image) / 3):
                new_image[4*j] += squares[(j, k)][0]
                new_image[4*j+1] += squares[(j, k)][1]
                new_image[4*j+2] += squares[(j, k)][2]
                new_image[4*j+3] += squares[(j, k)][3]


    image = tuple(new_image)

count = 0
for row in image:
    count += sum([1 for c in row if c == "#"])

print count
