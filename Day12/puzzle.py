class Move:
    direction = 1+0j
    position = 0+0j # also waypoint for puzzle 2
    ship_pos = 0+0j # puzzle 2
    def south(self, val): self.position -= val * 1j
    def north(self, val): self.position += val * 1j
    def east(self, val): self.position += val
    def west(self, val): self.position -= val
    def left(self, deg): 
        self.direction *= (1j)**(deg//90)
        if self.puzzle == 2: self.position *= (1j)**(deg//90)
    def right(self, deg): self.left(-deg)
    def forward(self, val): 
        if self.puzzle == 1: self.position += val * self.direction
        else: self.ship_pos += val * self.position
    moves = {'N': north, 'S': south, 'L': left, 'R': right,
             'W': west, 'E': east, 'F': forward}
    
    def __init__(self, str, puzzle=1):
        self.puzzle = puzzle
        if puzzle == 2: self.position = 10 + 1j
        self.instructions = [(self.moves[line[0]], int(line[1:])) for line in str.splitlines()]
    
    def run(self): 
        for inst in self.instructions: inst[0](self, inst[1])
        return self.dist()
    
    def dist(self): 
        real_pos = self.position if self.puzzle == 1 else self.ship_pos
        return int(abs(real_pos.real) + abs(real_pos.imag))

file_names = ['small_input', 'large_input']
folder_name = './Day12/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        data = input_file.read()
        puzzle1 = Move(data, puzzle=1)
        print(F'Puzzle 1 - {file_name}: ', puzzle1.run())
        puzzle2 = Move(data, puzzle=2)
        print(F'Puzzle 2 - {file_name}: ', puzzle2.run())
        