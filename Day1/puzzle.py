import numpy as np

"""
Puzzle 1:
Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

Puzzle 2:
Find three numbers in your expense report that meet the same criteria and then multiply those three numbers together.
"""

def puzzle1(list, total):
  for i, n1 in enumerate(list):
    for n2 in list[i+1:]:
      if n1+n2 == total:
        return n1*n2
  return 0

def puzzle2(list, total):
  n = len(list)
  for i in range(n):
    for j in range(i+1, n):
      for k in range(j+1, n):
        if list[i]+list[j]+list[k] == total:
          return list[i]*list[j]*list[k]
  return 0
  
def read_from_file(file):
  return [int(x) for x in file.read().splitlines()]

if __name__ == "__main__":
  total = 2020
  
  with open('./Day1/small_input') as small_file:
    list = read_from_file(small_file)
    print("Puzzle 1 - small input: ", puzzle1(list, total))
    print("Puzzle 2 - small input: ", puzzle2(list, total))

  with open('./Day1/large_input') as large_file:
    list = read_from_file(large_file)
    print("Puzzle 1 - small input: ", puzzle1(list, total))
    print("Puzzle 2 - small input: ", puzzle2(list, total))
    
  
