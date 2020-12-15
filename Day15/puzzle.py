input1 = [0,3,6]
input2 = [8,13,1,0,18,9]

def puzzle(input, target):
    last_index = {value: indx for indx, value in enumerate(input[:-1])}
    for i in range(len(input), target):
        if (last := input[-1]) in last_index:
            input.append(i - last_index[last] - 1)
        else: input.append(0)
        last_index[last] = i - 1
    return input[-1]

print(F"Puzzle 1: {puzzle(input2, 2020)}")
print(F"Puzzle 2: {puzzle(input2, 30000000)}")
