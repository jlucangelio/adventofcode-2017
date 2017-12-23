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

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

infected = defaultdict(lambda: False)

with open("day22.input") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            infected[(i-12,j-12)] = c == "#"

print infected[(0,0)]

cur = (0, 0)
d = UP
count = 0
for i in range(10000):
    print cur, infected[cur]
    if infected[cur]:
        d = turn_right(d)
    else:
        d = turn_left(d)

    if not infected[cur]:
        count += 1

    infected[cur] = not infected[cur]

    cur = (cur[0] + d[0], cur[1] + d[1])

print count
