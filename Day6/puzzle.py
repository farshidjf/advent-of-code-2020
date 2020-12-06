def extract_groups1(data):
    lines = data.splitlines()
    groups = [set()]
    i = 0
    for line in lines:
        if line:
            for l in line:
                groups[i].add(l)
        else:
            i += 1
            groups.append(set())
    return groups

def extract_groups2(data):
    from string import ascii_lowercase
    lines = data.splitlines()
    groups = [set(ascii_lowercase)]
    person = set()
    i = 0
    for line in lines:
        if line:
            person = set()
            for l in line:
                person.add(l)
            groups[i] = groups[i].intersection(person)
        else:
            i += 1
            groups.append(set(ascii_lowercase))
    return groups

file_names = ["small_input", "large_input"]
folder_name = "./Day6/"
for file_name in file_names:
    with open(folder_name + file_name) as file:
        data = file.read()
        for i, extract_groups in enumerate([extract_groups1, extract_groups2]):
            print(F"Puzzle {i} - {file_name}: ", sum([len(group) for group in extract_groups(data)]))
            