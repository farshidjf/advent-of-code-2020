test_input = [3,8,9,1,2,5,4,6,7]
main_input = [7,3,9,8,6,2,5,4,1]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedCycle:
    def __init__(self, lst):
        self.head = Node(lst[0])
        self.n = len(lst)
        current = self.head
        for value in lst[1:]:
            current.next = Node(value)
            current = current.next
        current.next = self.head
        self.lookup = [0] * (self.n + 1)
        for node in self:
            self.lookup[node.data] = node
    
    def step(self):
        first = self.head.next
        last = first.next.next
        self.head.next = last.next
        
        vals = [first.data, first.next.data, last.data]
        next_val = self.head.data - 1 if self.head.data > 1 else self.n
        while next_val in vals:
            next_val = next_val - 1 if next_val > 1 else self.n
        place = self.lookup[next_val]
        place_end = place.next
        place.next = first
        last.next = place_end
        self.head = self.head.next

    def __iter__(self):
        node = self.head
        while True:
            yield node
            node = node.next
            if node == self.head: break

def puzzle1():
    for inp in (test_input, main_input):
        cups = LinkedCycle(inp)
        for _ in range(100):
            cups.step()
        cups.head = cups.lookup[1]
        for i, node in enumerate(cups):
            if i == 0: out = ''
            else: out += str(node.data)
        print(F'Puzzle 1 - {inp}: ', out)

def puzzle2():
    for inp in (test_input, main_input):
        cups = LinkedCycle(inp + list(range(10, 1000_001)))
        for _ in range(10_000_000):
            cups.step()
        n1 = cups.lookup[1].next
        n2 = n1.next
        print(F'Puzzle 2 - {inp}: ', n1.data * n2.data)

puzzle1()
puzzle2()
