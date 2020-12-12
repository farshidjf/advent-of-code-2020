from copy import deepcopy

def parse_program(input_data):
    def parse_line(line):
        operator, operand = line.split()
        return [operator, int(operand)]
    return [parse_line(line) for line in input_data.splitlines()]

def run_program(program):
    n = len(program)
    visited = [False] * n
    current_line = 0
    accumulator = 0
    while current_line < n and not visited[current_line]:
        visited[current_line] = True
        operator, operand = program[current_line]
        if operator == 'nop':
            current_line += 1
        elif operator == 'acc':
            accumulator += operand
            current_line += 1
        elif operator == 'jmp':
            current_line += operand
    return ((current_line == n), accumulator)

def fix_program(program):
    jmp_or_nop_indices = [i for i, x in enumerate(program) if not x[0] == 'acc']
    def change_nop_jmp(operator):
        if operator == 'jmp': return 'nop'
        return 'jmp'
    for i in jmp_or_nop_indices:
        new_program = deepcopy(program)
        new_program[i][0] = change_nop_jmp(new_program[i][0])
        succeeded, accumulator = run_program(new_program)
        if succeeded:
            return accumulator
    return False

file_names = ['small_input', 'large_input']
folder_name = './Day8/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        program = parse_program(input_file.read())
        succeeded, accumulator = run_program(program)
        print(F'Puzzle 1 - {file_name}: ', accumulator)
        print(F'Puzzle 2 - {file_name}: ', fix_program(program))
