def calculate_weights(node, programs):
    weight, programs_above = programs[node]

    child_weights = []
    stack_weights = []
    total_weights = []
    for child in programs_above:
        child_weight, stack_weight = calculate_weights(child, programs)
        child_weights.append(child_weight)
        stack_weights.append(stack_weight)
        total_weights.append(child_weight + stack_weight)

    if len(programs_above) > 0:
        first_total_weight = total_weights[0]

        if any([tweight != first_total_weight for tweight in total_weights]):
            print child_weights
            print stack_weights
            print total_weights
            for i, wi in enumerate(total_weights):
                if all([wi != wj for j, wj in enumerate(total_weights) if j != i]):
                    # wi is different from all other weights
                    wj = total_weights[(i + 1) % 2]
                    print child_weights[i] + wj - wi
            print

    return weight, sum(total_weights)


programs = {}
programs_above_others = set()

with open("day7.input") as f:
    for line in f.readlines():
        tokens = line.strip().split()
        name = tokens[0]
        weight = int(tokens[1][1:-1])

        programs_above = []
        if len(tokens) > 3:
            for token in tokens[3:]:
                if token[-1] == ',':
                    programs_above.append(token[:-1])
                else:
                    programs_above.append(token)

            programs_above_others.update(programs_above)

        programs[name] = (weight, programs_above)

root = (set(programs.keys()) - programs_above_others).pop()

print root
print calculate_weights(root, programs)
