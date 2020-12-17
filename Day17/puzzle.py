from itertools import product
from copy import deepcopy

def read_initial_state(lines, dim):
    return {(i, j) + (0,)*(dim-2) for i, line in enumerate(lines)
                for j, c in enumerate(line) if c == '#'}

def cycle(actives, dim):
    actives_cp = deepcopy(actives)
    deltas = set(product((-1, 0, 1), repeat=dim)) - {(0,)*dim}
    
    def range_dim(d):
        dim_coord = {x[d] for x in actives}
        return tuple(range(min(dim_coord)-1, max(dim_coord)+2))

    def find_num_act_neighbors(coord):
        return sum([1 for delta in deltas if 
                        tuple(i+di for i, di in zip(coord, delta)) in actives])

    for coord in product(*(range_dim(d) for d in range(dim))):
        num_act_neighbors = find_num_act_neighbors(coord)
        if coord in actives:
            if not num_act_neighbors in {2,3}:
                actives_cp.remove(coord)
        elif num_act_neighbors == 3: actives_cp.add(coord)
        
    return actives_cp

def puzzle(actives, dim):
    for _ in range(6): actives = cycle(actives, dim)
    return len(actives)


file_names = ['small_input', 'large_input']
folder_name = './Day17/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        lines = input_file.readlines()
        actives = read_initial_state(lines, 3)
        print(F'Puzzle 1 - {file_name}: ', puzzle(actives, 3))
        actives = read_initial_state(lines, 4)
        print(F'Puzzle 2 - {file_name}: ', puzzle(actives, 4))
