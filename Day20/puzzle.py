from collections import deque
from functools import reduce

tiles = dict()
neighbors = dict()
n = 10

def read(inputs):
    for inp in inputs:
        lines = inp.splitlines()
        id = int(lines[0].split()[1][:-1])
        tiles[id] = [list(t) for t in lines[1:]]

def side(id, i):    # elements on the side i of tiles[id] in CCW order
    if i == 0:
        return [t[-1] for t in tiles[id]][::-1]
    if i == 1:
        return tiles[id][0][::-1]
    if i == 2:
        return [t[0] for t in tiles[id]]
    if i == 3:
        return tiles[id][-1]
    
def match(id1, id2, i1, i2):    # if side i1 of tiles[id1] matches side i2 of tiles[id2], returns whether we need flip the tiles to match
    s1, s2 = side(id1, i1), side(id2, i2)
    if all([s == ss for s, ss in zip(s1, s2)]):
        return -1
    if all([s == ss for s, ss in zip(s1, s2[::-1])]):
        return 1
    return 0

def rotate(id, rotation):   # rotate tiles[id] by i*pi/2 CCW
    if rotation == 1:
        tiles[id] = [[tiles[id][j][n-i-1] for j in range(n)] for i in range(n)]
    if rotation == 2:
        tiles[id] = [[tiles[id][n-i-1][n-j-1] for j in range(n)] for i in range(n)]
    if rotation == 3:
        tiles[id] = [[tiles[id][n-j-1][i] for j in range(n)] for i in range(n)]

def adjust(id, i1, i2, flip):   # rotate tiles[id] to match its i2 side with i1 side of another tile, flip if needed
    rotate(id, (i1 - i2 + 2) % 4)
    if flip == -1:
        if i1 % 2 == 0:     # flip vertically
            tiles[id].reverse()
        else:               # flip horizontally
            tiles[id] = [t[::-1] for t in tiles[id]]
    

def find_match(id, i):      # find a tile matching side i of tiles[id] if exist
    for id2 in list(tiles.keys()):
        if id2 != id and not id2 in neighbors[id]: #not id2 in connected:
            for i2 in range(4):
                if (flip := match(id, id2, i, i2)) != 0:
                    return id2, i2, flip
    return 0, 0, 0


def assemble():     # find all matching neighbors of all tiles and their correct orientation
    global neighbors
    neighbors = {id: [-1]*4 for id in tiles.keys()} # [right, up, left, down]
    first = min(tiles.keys())
    connected = {first}
    queue = deque([first])
    while queue:
        id = queue.popleft()
        for i in range(4):
            if neighbors[id][i] == -1:
                id2, i2, flip = find_match(id, i)
                neighbors[id][i] = id2
                if id2 != 0:
                    neighbors[id2][(i+2) % 4] = id
                    if id2 not in connected:
                        adjust(id2, i, i2, flip)
                        connected.add(id2)
                        queue.append(id2)

def find_corners(): # for puzzle 1
    return [id for id in neighbors.keys() if neighbors[id].count(0) == 2]

def count_columns(left):
    count = 1
    while (left := neighbors[left][0]) != 0: count += 1
    return count
def count_rows(top):
    count = 1
    while (top := neighbors[top][3]) != 0: count += 1
    return count
def build_grid(num_row, num_col, corner):
    left = corner
    grid = dict()
    for i in range(num_row):
        current = left
        for j in range(num_col):
            grid[(i, j)] = tiles[current]
            current = neighbors[current][0]
        left = neighbors[left][3]
    return grid

def trim_and_glue():
    for id in tiles.keys():
        tiles[id] = [t[1:-1] for t in tiles[id][1:-1]]
    top_left_corner = [id for id in neighbors.keys() if neighbors[id][1] == neighbors[id][2] == 0][0]
    num_col = count_columns(top_left_corner)
    num_row = count_rows(top_left_corner)
    grid = build_grid(num_row, num_col, top_left_corner)
    picture = [['.'] * (num_col * (n-2)) for _ in range(num_row * (n-2))] 
    for r in range(num_row):
        for c in range(num_col):
            for i in range(n-2):
                for j in range(n-2):
                    picture[r*(n-2)+i][c*(n-2)+j] = grid[(r, c)][i][j]
    return picture

sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()

def search_for_monster(picture, monster):
    M, N = len(picture), len(picture[0])
    m, n = len(monster), len(monster[0])
    found = False
    mask = {(i, j) for i, line in enumerate(monster) for j, c in enumerate(line) if c =='#'}
    for ii in range(M - m):
        for jj in range(N - n):
            if all(picture[i + ii][j + jj] == '#' for i, j in mask):
                for i, j in mask:
                    picture[i + ii][j + jj] = 'O'
                found = True
    return found

def give_all_rotations(monster):
    monsters = [monster.copy()]
    for _ in range(3):  # add three rotations
        m = len(monsters[-1])
        n = len(monsters[-1][0])
        monsters.append([[monsters[-1][j][n-i-1] for j in range(m)] for i in range(n)])
    for i in range(4):  # add refletions of all rotations
        monsters.append(monsters[i][::-1])
    return monsters

def puzzle2(picture):
    monsters = give_all_rotations(sea_monster)
    for monster in monsters:
        if search_for_monster(picture, monster):
            break
    return ''.join([''.join(p) for p in picture]).count('#')

with open('./Day20/large_input') as input:
    read(input.read().split('\n\n'))
    assemble()
    print('Puzzle 1: ', reduce(lambda x, y: x*y, find_corners()))
    picture = trim_and_glue()
    print('Puzzle 2: ', puzzle2(picture))
