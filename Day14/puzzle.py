import re

def apply_mask1(mask, number):  # puzzle 1
    bin_list = list(format(number, '036b'))
    for i in range(36):
        if mask[i] == '0': bin_list[i] = '0'
        if mask[i] == '1': bin_list[i] = '1'
    return int("".join(bin_list), 2)

def run1(code): # puzzle 1
    mem = dict()
    for line in code.splitlines():
        if m := re.match(r'^mask = (?P<mask>.{36})$', line):
            mask = list(m.group('mask'))
        if m := re.match(r'^mem\[(?P<address>\d+)\] = (?P<value>.+)$', line):
            mem[m.group('address')] = apply_mask1(mask, int(m.group('value')))
    return sum(mem.values())

def apply_mask2(mask, number):  # puzzle 2
    bin_lists = [list(format(number, '036b'))]
    for i in range(36):
        if mask[i] == 'X': 
            temp = []
            for b in bin_lists:
                b[i] = '0'
                temp.append(b.copy())
                b[i] = '1'
            bin_lists += temp
        if mask[i] == '1': 
            for b in bin_lists: b[i] = '1'
    return [int("".join(b), 2) for b in bin_lists]

def run2(code): # puzzle 2
    mem = dict()
    for line in code.splitlines():
        if m := re.match(r'^mask = (?P<mask>.{36})$', line):
            mask = list(m.group('mask'))
        if m := re.match(r'^mem\[(?P<address>\d+)\] = (?P<value>.+)$', line):
            addresses = apply_mask2(mask, int(m.group('address')))
            for address in addresses:
                mem[address] = int(m.group('value'))
    return sum(mem.values())


file_names = ['small_input', 'large_input']
folder_name = './Day14/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        code = input_file.read()
        print(F'Puzzle 1 - {file_name}: ', run1(code))
        if file_name == "large_input":
            print(F'Puzzle 2 - {file_name}: ', run2(code))
