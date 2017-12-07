with open("day4_1.input") as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        words = line.strip().split()
        if len(set(words)) == len(words):
            count += 1

print count


with open("day4_1.input") as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        words = line.strip().split()

        found_anagram = False
        for i, w in enumerate(words):
            for j, y in enumerate(words):
                if i < j:
                    if set(w) == set(y):
                        found_anagram = True

        if not found_anagram:
            count += 1

print count
