from itertools import takewhile, count, product

class WaitingRoom:
    def __init__(self, str, puzzle=1):
        self.puzzle = puzzle
        self.state = [row for row in str.splitlines()]
        self.nr = len(self.state)
        self.nc = len(self.state[0])
        neighbors = self.neighbors1 if puzzle == 1 else self.neighbors2
        self.neighbors = [[list(neighbors(i, j)) for j in range(self.nc)] for i in range(self.nr)]
        
    def is_occupied(self, i, j): return self.state[i][j] == '#'
    def is_empty(self, i, j): return self.state[i][j] == 'L'
    def is_seat(self, i, j): return self.state[i][j] != '.'
    def is_in_range(self, i, j): return 0 <= i < self.nr and 0 <= j < self.nc
    
    deltas = set(product((-1,0,1), repeat=2))-{(0,0)}    # [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (1,-1), (-1,1)]

    def neighbors1(self, i, j): # puzzle 1
        return [(i+di, j+dj) for di, dj in self.deltas if self.is_in_range(i+di, j+dj)]
    
    def neighbors2(self, i, j): # puzzle 2
        return filter(lambda x: x is not None, 
                      [next(((ii, jj) for ii, jj in 
                                        takewhile(lambda x: self.is_in_range(*x),
                                                  ((i+n*di, j+n*dj) for n in count(1)) )
                                      if self.is_seat(ii, jj)), None) 
                       for di, dj in self.deltas])
        
    def occupied_neighbors(self, i, j):
        return [(i, j) for i, j in self.neighbors[i][j] if self.is_occupied(i, j)]
    
    def occupy(self, state, i, j): 
        row = list(state[i])
        row[j] = '#'
        state[i] = "".join(row)
    def empty(self, state, i, j): 
        row = list(state[i])
        row[j] = 'L'
        state[i] = "".join(row)

    def update_step(self):
        threshold = 4 if self.puzzle == 1 else 5
        state = self.state.copy()
        for i in range(self.nr):
            for j in range(self.nc):
                if self.is_empty(i, j) and len(self.occupied_neighbors(i, j)) == 0:
                    self.occupy(state, i, j)
                if self.is_occupied(i, j) and len(self.occupied_neighbors(i, j)) >= threshold:
                    self.empty(state, i, j)
        return state
    
    def run(self):
        state = self.update_step()
        while self.state != state:    
            self.state = state
            state = self.update_step()
        return self.count_occupied_seats()
    
    def count_occupied_seats(self):
        return sum([1 for row in range(self.nr)
                      for column in range(self.nc) if self.is_occupied(row, column)])

file_names = ['small_input', 'large_input']
folder_name = './Day11/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        data = input_file.read()
        puzzle1 = WaitingRoom(data, puzzle=1)
        print(F'Puzzle 1 - {file_name}: ', puzzle1.run())
        puzzle2 = WaitingRoom(data, puzzle=2)
        print(F'Puzzle 2 - {file_name}: ', puzzle2.run())
