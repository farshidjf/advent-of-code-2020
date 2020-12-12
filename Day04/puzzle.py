def extract_passports(data):
    def parse(passport_data):
        passport = dict()
        for data in passport_data:
            (field, value) = data.split(':')
            passport[field] = value
        return passport
    passports = []
    passport_data = []
    for line in data.splitlines():
        if line == "":
            passports.append(parse(passport_data))
            passport_data = []
        else:
            passport_data += line.split()
    passports.append(parse(passport_data))
    return passports

required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'] # not 'cid'
def verify1(passport):
    return all([field in passport for field in required_fields])

def verify2(passport):
    if not verify1(passport):
        return False
    from re import match
    _is_valid_year = lambda str, first, last: match(r"^\d{4}$", str) and first <= int(str) <= last
    valid = dict()
    valid['byr'] = _is_valid_year(passport['byr'], 1920, 2002)
    valid['iyr'] = _is_valid_year(passport['iyr'], 2010, 2020)
    valid['eyr'] = _is_valid_year(passport['eyr'], 2020, 2030)
    if match(r"^\d{2}in$", passport['hgt']):
        valid['hgt'] = 59 <= int(passport['hgt'][:2]) <= 76
    elif match(r"^\d{3}cm$", passport['hgt']):
        valid['hgt'] = 150 <= int(passport['hgt'][:3]) <= 193
    else: valid['hgt'] = False
    valid['hcl'] = bool(match(r"^#([\da-f]){6}$", passport['hcl']))
    valid['ecl'] = passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    valid['pid'] = bool(match(r"^\d{9}$", passport['pid']))
    return all(valid.values()) 

file_names = ["small_input", "large_input"]
folder_name = "./Day4/"
for file_name in file_names:
    with open(folder_name + file_name) as file:
        passports = extract_passports(file.read())
        for i, verify in enumerate([verify1, verify2]):
            print(F"Puzzle {i} - {file_name}: ", len([1 for passport in passports if verify(passport)]))
