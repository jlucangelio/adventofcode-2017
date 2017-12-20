from collections import namedtuple

def move(p, d):
    return Position(p.x + d.x, p.y + d.y)


def get(m, p):
    return m[p.x][p.y]

def printable_pos(p):
    return Position(p.x + 1, p.y + 1)

MAP = []

with open("day19.input") as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        MAP.append([c for c in line])

print MAP

Position = namedtuple("Position", "x y")
cur_pos = Position(0, 27)

DOWN = Position(1, 0)
UP = Position(-1, 0)
LEFT = Position(0, -1)
RIGHT = Position(0, 1)

direction = DOWN

if MAP[0][27] != "|":
    print "ERROR"

word = []
count = 0
while True:
    count += 1
    # print printable_pos(cur_pos), get(MAP, cur_pos), direction
    n_pos = move(cur_pos, direction)
    n_map = MAP[n_pos.x][n_pos.y]
    if direction == DOWN or direction == UP:
        if n_map == "|":
            cur_pos = n_pos
        elif n_map == "-":
            # Crossing over.
            cur_pos = n_pos
        elif str.isalpha(n_map):
            word.append(n_map)
            cur_pos = n_pos
        elif n_map == "+":
            # Where to turn?
            left_pos = move(n_pos, LEFT)
            left = get(MAP, left_pos)
            right_pos = move(n_pos, RIGHT)
            right = get(MAP, right_pos)
            if left == "-":
                direction = LEFT
            elif right == "-":
                direction = RIGHT
            else:
                print "error: can't turn at", n_pos, n_map, left, right
                print "coming", direction
                break
            cur_pos = n_pos
        elif n_map == " ":
            print "dead end"
            break

    elif direction == LEFT or direction == RIGHT:
        if n_map == "-":
            cur_pos = n_pos
        elif n_map == "|":
            # Crossing over.
            cur_pos = n_pos
        elif str.isalpha(n_map):
            word.append(n_map)
            cur_pos = n_pos
        elif n_map == "+":
            # Where to turn?
            up_pos = move(n_pos, UP)
            up = get(MAP, up_pos)
            down_pos = move(n_pos, DOWN)
            down = get(MAP, down_pos)
            if up == "|":
                direction = UP
            elif down == "|":
                direction = DOWN
            else:
                print "error: can't turn at", n_pos, n_map, up, down
                print "coming", direction
                break
            cur_pos = n_pos
        elif n_map == " ":
            print "dead end", n_pos
            break

print word
print "".join(word)
print count