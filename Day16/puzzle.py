import re

def read_from_file(input):
    rules = dict()
    tickets = []
    for line in input.readlines():
        if m := re.match(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', line):
            field, a1, b1, a2, b2 = m.groups()
            rules[field] = lambda x, a1=int(a1), b1=int(b1), a2=int(a2), b2=int(b2): a1 <= x <= b1 or a2 <= x <= b2
        if re.match(r'^(\d+)(,\s*\d+)*', line):
            tickets.append([int(x) for x in line.split(',')])
    return rules, tickets[0], tickets[1:]
    

def is_invalid(n, rules):
    return not any([rule(n) for rule in rules.values()])

def invalid_values(tickets, rules):
    return [n for ticket in tickets for n in ticket if is_invalid(n, rules)]

def remove_invalid(tickets, rules):
    return [ticket for ticket in tickets if not any([is_invalid(n, rules) for n in ticket])]


def find_fields(tickets, rules):
    num_fields = len(rules)
    tickets = remove_invalid(tickets, rules)
    possible_fields = [set(rules.keys())]*num_fields
    for i in range(num_fields):
        for ticket in tickets:
            possible_fields[i] = possible_fields[i] & {field for field, rule in rules.items() if rule(ticket[i])}
    resolved = [False]*num_fields
    while not all(resolved):
        to_resolve = next(i for i, pf in enumerate(possible_fields) if len(pf) == 1 and not resolved[i])
        resolved[to_resolve] = True
        for i in range(num_fields): 
            if not resolved[i]:
                possible_fields[i] = possible_fields[i] - possible_fields[to_resolve]
    return [next(iter(pf)) for pf in possible_fields]

            
def find_departure_product(ticket, fields):
    prod = 1
    for i, field in enumerate(fields):
        if re.match('departure', field):
            prod *= ticket[i]
    return prod


file_name = 'large_input'
folder_name = './Day16/'
with open(folder_name+file_name) as input_file:
    rules, my_ticket, other_tickets = read_from_file(input_file)
    print('Puzzle 1: ', sum(invalid_values(other_tickets, rules)))
    fields = find_fields([my_ticket]+other_tickets, rules)
    print('Puzzle 2: ', find_departure_product(my_ticket, fields))
