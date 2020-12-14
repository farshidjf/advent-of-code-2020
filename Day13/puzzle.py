from functools import reduce
from itertools import count

def puzzle1(time_stamp, bus_IDs):
    wait = 1e10 # a large number
    for id in bus_IDs:
        if (w := (id - (time_stamp % id)) % id) < wait:
            wait = w
            best_id = id
    return wait * best_id

def gcd(a, b):
    while(b): a, b = b, a % b
    return a
def lcm(a, b): return (a * b) // gcd(a, b)
def list_lcm(lst): return reduce(lcm, lst)

def puzzle2_using_CRT(bus_IDs): # first attempt
    def gcdExtended(a, b):  # return g = gcd(a,b) and x and y such that ax+by=g
        if a == 0: return b, 0, 1
        gcd, x1, y1 = gcdExtended(b % a, a)
        x = y1 - (b//a) * x1
        y = x1
        return gcd, x, y

    n = 0
    product = reduce(lambda x, y: x * y, bus_IDs.values())
    for i, v in bus_IDs.items():    # Chinese Remainder Theorem for non-coprime values
        V = product//v
        gcd_v, M, _ = gcdExtended(V, v)
        n -= i * V * M // gcd_v
    
    assert all((n+i) % id == 0 for i, id in bus_IDs.items()) # lol, making sure the algorithm works
    
    return n % list_lcm(bus_IDs.values())

def puzzle2_attempt2(bus_IDs):  # without CRT
    def solve_for_two(X1, r1, X2, r2): 
        """search in numbers n of the form a*X1-r1 to 
        find one that is also in the form n = b*X2-r2"""
        for n in count(-r1, X1):
            if (n+r2) % X2 == 0:
                return n
    
    # Here is the main idea: suppose you find n = solve_for_two(X1,X2) to find the solution for the
    # third number, we need to do a similar search for some n' = b'*X3-r3 such that it still has
    # the same remainders to X1 and X2.
    # If we search for n' of the form n' = n + a'*lcm(X1,X2), remainders of n' by X1 and X2 stay the
    # same because adding any multiples of X1 and X2 would not change the remainder, the smallest of 
    # such multiple is obviously their Least Common Multiple.
    # Since solve_for_two searches for a satisfying n = -r1 + a*X1 that also satisfies n = b*X2-r2,
    # we could use that to solve for n' = solve_for_two(-n, lcm(X1, X2), X3, r3)
        
    r1 = next(iter(bus_IDs))
    X1 = bus_IDs[r1]
    bus_IDs.pop(r1)
    for r2, X2 in bus_IDs.items():
        n = solve_for_two(X1, r1, X2, r2)
        r1 = -n
        X1 = lcm(X1, X2)
    
    assert all((n+i) % id == 0 for i, id in bus_IDs.items()) # making sure the algorithm works
    
    return n
    


file_names = ['small_input', 'large_input']
folder_name = './Day13/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        time_stamp = int(input_file.readline())
        bus_IDs = {i: int(id) for i, id in enumerate(input_file.readline().split(',')) if id.isnumeric()}        
        print(F'Puzzle 1 - {file_name}: ', puzzle1(time_stamp, bus_IDs.values()))
        print(F'Puzzle 2 - {file_name}: ', puzzle2_attempt2(bus_IDs))
