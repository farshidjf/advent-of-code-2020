from collections import deque

def in_preamble(n, preamble):
    for i in range(len(preamble)-1):
        for j in range(i+1, len(preamble)):
            if n == preamble[i] + preamble[j]:
                return True
    return False

def find_first_violation(seq, preamble_size):
    preamble = deque(seq[:preamble_size])
    for i in range(preamble_size, len(seq)):
        if in_preamble(seq[i], preamble):
            preamble.append(seq[i])
            preamble.popleft()
        else: return seq[i]
    
def find_contiguous_set(seq, key):
    for i in range(len(seq)):
        for delta_i in range(len(seq)-i):
            if sum(seq[i:i+delta_i]) == key:
                return min(seq[i:i+delta_i]) + max(seq[i:i+delta_i])
    return 0

file_names = ['small_input', 'large_input']
folder_name = './Day9/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        preamble_size = 5 if file_name == 'small_input' else 25
        seq = [int(line) for line in input_file.readlines()]
        key = find_first_violation(seq, preamble_size)
        print(F'Puzzle 1 - {file_name}: ', key)
        print(F'Puzzle 2 - {file_name}: ', find_contiguous_set(seq,key))
