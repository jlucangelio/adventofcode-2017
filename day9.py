with open("day9.input") as f:
    INPUT = f.read()

in_garbage = False
in_excl = False

groups = []
score = 1
total_score = 0
total_garbage = 0

for c in INPUT:
    # print in_garbage, in_excl

    if in_excl:
        in_excl = False
        continue

    if c == "{":
        if in_garbage:
            total_garbage += 1
            continue

        groups.append(score)
        total_score += score
        score += 1
    elif c == "}":
        if in_garbage:
            total_garbage += 1
            continue

        in_group = False
        groups.pop()
        score -= 1
    elif c == "<":
        if in_garbage:
            total_garbage += 1
            continue

        in_garbage = True
    elif c == ">":
        if in_garbage:
            in_garbage = False
    elif c == "!":
        in_excl = True
    elif c == ",":
        if in_garbage:
            total_garbage += 1

    else:
        if in_garbage:
            total_garbage += 1

print groups
print total_score
print total_garbage
