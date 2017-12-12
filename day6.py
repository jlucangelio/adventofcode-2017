INPUT = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
# INPUT =[0, 2, 7, 0]

state = INPUT
configs = {tuple(INPUT): 0}
redist = 0

while True:
    max_index, max_value = max(enumerate(state), key=lambda e: e[1])

    state[max_index] = 0
    cur_index = max_index + 1
    blocks_left = max_value

    while blocks_left > 0:
        state[cur_index % len(state)] += 1
        cur_index += 1
        blocks_left -= 1

    redist += 1

    if tuple(state) in configs:
        print redist - configs[tuple(state)]
        break

    configs[tuple(state)] = redist

print redist
