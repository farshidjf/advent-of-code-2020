import re
from collections import Counter

coord = {'e': 2, 'w': -2, 'ne': 1+1j, 'nw': -1+1j, 'se': 1-1j, 'sw': -1-1j}

def read_input(input):
    return [sum([coord[dir] for dir in re.findall(r'(e|w|ne|nw|se|sw)', line)])
            for line in input.splitlines()]

def next_day(blacks):
    def white_neighbors(tile):
        return (tile + dir for dir in coord.values() if tile + dir not in blacks)
    def num_black_neighbors(tile):
        return sum(1 for dir in coord.values() if tile+dir in blacks)
    remain_black = {black for black in blacks if num_black_neighbors(black) in (1,2)}
    flip_to_black = set()
    for black in blacks:
        for white in white_neighbors(black):
            if white not in flip_to_black and num_black_neighbors(white) == 2:
                flip_to_black.add(white)
    return remain_black.union(flip_to_black)

file_names = ['small_input', 'large_input']
folder_name = './Day24/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        tiles = read_input(input_file.read())
        flip_counts = Counter(tiles)
        blacks = {tile for tile, count in flip_counts.items() if count % 2 == 1}
        print(F'Puzzle 1 - {file_name}: ', len(blacks))
        for _ in range(100): blacks = next_day(blacks)
        print(F'Puzzle 2 - {file_name}: ', len(blacks))
