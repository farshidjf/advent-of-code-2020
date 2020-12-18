from functools import reduce

def operate_simple(xs, ops):
    x = xs[0]
    for y, op in zip(xs[1:], ops):
        if op == '+': x += y
        if op == '*': x *= y
    return x

def operate_addition_first(xs, ops):
    while True:
        try:
            i = ops.index('+')
            ops.pop(i)
            xs = xs[:i] + [xs[i] + xs[i+1]] + xs[i+2:]
        except: break
    return reduce((lambda x, y: x*y), xs)
    
def evaluate(str, addition_first):
    operate = operate_addition_first if addition_first else operate_simple
    i = 0
    xs = []
    ops = []
    while i < len(str):
        c = str[i]
        if c == '(': 
            x, ii = evaluate(str[i+1:], addition_first)
            i += ii+1
            xs.append(x)
        elif c == ')': break
        elif c in {'+', '*'}: ops.append(c)
        elif '0' <= c <= '9': xs.append(int(c))
        i += 1
    return operate(xs, ops), i

with open('./Day18/large_input') as input:
    lines = input.readlines()
    print('Puzzle 1: ', sum([evaluate(line, False)[0] for line in lines]))
    print('Puzzle 2: ', sum([evaluate(line, True)[0] for line in lines]))
