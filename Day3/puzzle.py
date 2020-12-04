def puzzle1(data, x_step, y_step):
    m = len(data)
    n = len(data[0])
    count = 0
    x = 0
    y = 0
    while(y < m):
        if (data[y][x] == '#'): 
            count += 1
        x = (x + x_step) % n
        y += y_step
    return count

def puzzle2(data):
    steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    product = 1
    for x_step, y_step in steps:
        product *= puzzle1(data, x_step, y_step)
    return product

with open('./Day3/small_input') as small_input:
    data = small_input.read().splitlines()
    print('Puzzle 1 - small input: ', puzzle1(data, 3, 1))
    print('Puzzle 2 - small input: ', puzzle2(data))

with open('./Day3/large_input') as large_input:
    data = large_input.read().splitlines()
    print('Puzzle 1 - large input: ', puzzle1(data, 3, 1))
    print('Puzzle 2 - large input: ', puzzle2(data))
