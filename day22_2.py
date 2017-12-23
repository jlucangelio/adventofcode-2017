from collections import defaultdict

def turn_left(d):
    if d == UP:
        return LEFT
    if d == LEFT:
        return DOWN
    if d == DOWN:
        return RIGHT
    if d == RIGHT:
        return UP


def turn_right(d):
    if d == UP:
        return RIGHT
    if d == RIGHT:
        return DOWN
    if d == DOWN:
        return LEFT
    if d == LEFT:
        return UP


def flip(d):
    if d == UP:
        return DOWN
    if d == LEFT:
        return RIGHT
    if d == DOWN:
        return UP
    if d == RIGHT:
        return LEFT

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

WEAKENED = "W"
FLAGGED = "F"

infected = defaultdict(lambda: ".")

with open("day22.input") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            infected[(i-12,j-12)] = c

print infected[(0,0)]

cur = (0, 0)
d = UP
count = 0
for i in range(10000000):
    if i % 100000 == 0:
        print i

    # print cur, infected[cur]
    if infected[cur] == "#":
        d = turn_right(d)
    elif infected[cur] == ".":
        d = turn_left(d)
    elif infected[cur] == "F":
        d = flip(d)

    if infected[cur] == "#":
        infected[cur] = "F"

    elif infected[cur] == "F":
        infected[cur] = "."

    elif infected[cur] == ".":
        infected[cur] = "W"

    elif infected[cur] == "W":
        infected[cur] = "#"
        count += 1

    cur = (cur[0] + d[0], cur[1] + d[1])

print count
