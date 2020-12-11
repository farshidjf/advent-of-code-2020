from itertools import takewhile

class WaitingRoom:
    def __init__(self, str, puzzle=1):
        self.puzzle = puzzle
        self.state = [row for row in str.splitlines()]
        self.nr = len(self.state)
        self.nc = len(self.state[0])
        neighbor_fun = self.neighbors if puzzle == 1 else self.neighbors2
        self.neighbor_list = [[list(neighbor_fun(i, j)) for j in range(self.nc)] for i in range(self.nr)]
        
    def is_occupied(self, i, j): return self.state[i][j] == '#'
    def is_empty(self, i, j): return self.state[i][j] == 'L'
    def is_seat(self, i, j): return self.state[i][j] != '.'
    def is_in_range(self, i, j): return 0 <= i < self.nr and 0 <= j < self.nc
    
    def neighbors(self, i, j): # puzzle 1
        return [(row, column)   
                    for row in range(max(i-1, 0), min(i+1+1, self.nr))
                        for column in range(max(j-1, 0), min(j+1+1, self.nc))
                            if (row, column) != (i, j) and self.is_seat(row, column)]
    
    def neighbors2(self, i, j): # puzzle 2, feeling functional today
        delta = [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (1,-1), (-1,1)]
        return filter(lambda x: x is not None, 
                      [next(((ii, jj) for ii, jj in 
                                        takewhile(lambda x: self.is_in_range(*x),
                                                  ((i+n*di, j+n*dj) for n in range(1, max(self.nr,self.nc))) )
                                      if self.is_seat(ii, jj)), None) 
                       for di, dj in delta])
        
    def occupied_neighbors(self, i, j):
        return [(i, j) for i, j in self.neighbor_list[i][j] if self.is_occupied(i, j)]
    
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
    
    def count_occupied_seats(self):
        return sum([1 for row in range(self.nr)
                      for column in range(self.nc) if self.is_occupied(row, column)])

file_names = ['small_input', 'large_input']
folder_name = './Day11/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        data = input_file.read()
        room1 = WaitingRoom(data, puzzle=1)
        room1.run()
        print(F'Puzzle 1 - {file_name}: ', room1.count_occupied_seats())
        room2 = WaitingRoom(data, puzzle=2)
        room2.run()
        print(F'Puzzle 2 - {file_name}: ', room2.count_occupied_seats())
