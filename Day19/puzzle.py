import re
from copy import deepcopy

def get_rules(rules_str):
    def str2tuple(lst_str):
        return tuple(int(x) for x in lst_str.strip().split(' '))
    rules = {}
    for line in rules_str.splitlines():
        if (m := re.match(r'^(?P<i>\d+):(?P<list>(?:\s\d+)+)$', line)):
            rules[int(m.group('i'))] = {str2tuple(m.group('list'))}
        if (m := re.match(r'^(?P<i>\d+):(?P<first>(?: \d+)+) \|(?P<second>(?: \d+)+)$', line)):
            rules[int(m.group('i'))] = {str2tuple(m.group('first')), str2tuple(m.group('second'))}
        if (m := re.match(r'^(\d+): "(\w)"$', line)):
            rules[int(m.groups()[0])] = {m.groups()[1]}
    return rules

def is_resolved(rule):
    return all(isinstance(r, str) for r in rule)

def substitute(key, rule1, rule2):
    try:
        i = rule2.index(key)
        temp = set()
        for sub in rule1:
            temp.add(tuple(r if k != i else sub for k, r in enumerate(rule2)))
        return set().union(*(substitute(key, rule1, rule) for rule in temp))
    except: 
        return {rule2}
        
def join(rule):
    if is_resolved(rule):
        return "".join(rule)
    else: return rule

def resolve(rules):
    resolved_rules = {}
    resolving = {}
    unresolved_rules = deepcopy(rules)
    for key, rule in rules.items():
        if is_resolved(rule):
            resolving[key] = rule
            unresolved_rules.pop(key)

    while 0 in unresolved_rules:
        for key1, rule1 in resolving.items():
            for key2 in unresolved_rules.keys():
                unresolved_rules[key2] = set().union(*(substitute(key1, rule1, rule) for rule in unresolved_rules[key2]))                
                unresolved_rules[key2] = {join(rule) for rule in unresolved_rules[key2]}
            resolved_rules[key1] = rule1
        resolving = {}
        
        for key in list(unresolved_rules.keys()):
            if is_resolved(unresolved_rules[key]):
                resolving[key] = unresolved_rules[key]
                unresolved_rules.pop(key)

    resolved_rules.update(resolving)
    return resolved_rules

def match_puzzle2(r42, r31, message): 
    # 0 = 8 11 = (42) (42+) (31+) (with number of repeats in 42+ should be at least equal to that of 31+)
    # all strings matching in rules 42 and 31 have length 8
    if len(message) % 8 != 0: return False
    n = len(message) // 8
    i = 0
    while i < n:
        if not message[i*8:(i+1)*8] in r42:
            break
        i += 1
    if  i < 2 or i == n or i < (n+1)/2: return False
    while i < n:
        if not message[i*8:(i+1)*8] in r31:
            return False
        i += 1
    return True

def puzzle1(messages, r0):
    return sum(1 for message in messages if message in r0)

def puzzle2(messages, r42, r31):
    return sum(1 for message in messages if match_puzzle2(r42, r31, message))

file_name = 'large_input'
folder_name = './Day19/'
with open(folder_name+file_name) as input_file:
    rules_str, messages = input_file.read().split('\n\n')
    messages = messages.splitlines()
    rules = get_rules(rules_str)
    r_rules = resolve(rules)
    print('Puzzle 1: ', puzzle1(messages, r_rules[0]))
    print('Puzzle 2:', puzzle2(messages, r_rules[42], r_rules[31]))
