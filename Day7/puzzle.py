import re

def get_bag_structure(input):
    def split_to_tuple(num_bag):
        num, bag = num_bag.split(' ',1)
        if num.isnumeric():
            return (bag, int(num))
        return ('',0)
    keys = [re.split(r' bags?\.', line)[0].split(" bags contain ")[0] for line in input.splitlines()]
    values = [list(map(split_to_tuple, re.split(r" bags?, ", re.split(r' bags?\.', line)[0].split(" bags contain ")[1]))) for line in input.splitlines()]
    return {key: value for key, value in zip(keys, values)}

def set_of_outer_bags(bag, bag_struct):
    outers = set()
    for outer in bag_struct:
        inners = [bag for bag,_ in bag_struct[outer]]
        if bag in inners:
            outers.add(outer)
            outers = outers.union(set_of_outer_bags(outer, bag_struct))
    return outers

def count_bags_inside(bag, bag_struct):
    if bag == '': return 0
    count = 0
    for inner in bag_struct[bag]:
        count += inner[1] * (1 + count_bags_inside(inner[0], bag_struct))
    return count
    
file_names = ['small_input', 'large_input']
folder_name = './Day7/'
for file_name in file_names:
    with open(folder_name+file_name) as input:
        bag = 'shiny gold'
        bag_struct = get_bag_structure(input.read())
        print(F'Puzzle 1 - {file_name}: ', len(set_of_outer_bags(bag, bag_struct)))
        print(F'Puzzle 2 - {file_name}: ', count_bags_inside(bag, bag_struct))
