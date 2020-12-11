def extract_ID(data):
    to_binary = [('F','0'), ('B','1'), ('L','0'), ('R','1')]
    for char, digit in to_binary:
        data = data.replace(char, digit)
    seats = data.splitlines()
    seat_IDs = [0]*len(seats)
    for i, seat in enumerate(seats):
        seat_IDs[i] = int(seat[:7], 2) * 8 + int(seat[7:], 2)
    return seat_IDs

def find_missing_ID(IDs):
    first = min(IDs)
    last = max(IDs)
    missing_IDs = [False]*(last-first+1)
    for id in IDs:
        missing_IDs[id-first] = True
    return missing_IDs.index(False)+first

file_name = "large_input"
folder_name = "./Day5/"
with open(folder_name + file_name) as file:
    seat_IDs = extract_ID(file.read())
    print("Puzzle 1: ", max(seat_IDs))
    print("Puzzle 2: ", find_missing_ID(seat_IDs))
