from collections import deque
from functools import lru_cache

@lru_cache(maxsize=1000)
def count_arrangements(adaptors):
    adaptors = deque(adaptors)
    head = adaptors.popleft()
    count = 0
    while adaptors[0] - head <= 3:
        if len(adaptors) == 1: return count+1
        count += count_arrangements(tuple(adaptors))
        adaptors.popleft()
    return count

def puzzle1(adaptors):
    diffs = [x - y for x, y in zip(adaptors[1:], adaptors[:-1])]
    return diffs.count(1) * diffs.count(3)

file_names = ['small_input', 'large_input']
folder_name = './Day10/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        adaptors = sorted([int(line) for line in input_file.readlines()] + [0])
        adaptors += [max(adaptors)+3] 
        print(F'Puzzle 1 - {file_name}: ', puzzle1(adaptors))
        print(F'Puzzle 2 - {file_name}: ', count_arrangements(tuple(adaptors)))
