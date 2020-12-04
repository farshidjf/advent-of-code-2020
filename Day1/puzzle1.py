import numpy as np


def puzzle1(list, total):
  for i, n1 in enumerate(list):
    for n2 in list[i+1:]:
      if n1+n2 == total:
        return n1*n2
  return 0
  
def read_from_file(file):
  return [int(x) for x in file.read().splitlines()]

if __name__ == "__main__":
  total = 2020
  
  with open('./Day1/small_input') as small_file:
    list = read_from_file(small_file)
    print("small input: ", puzzle1(list, total))

  with open('./Day1/large_input') as large_file:
    list = read_from_file(large_file)
    print("small input: ", puzzle1(list, total))
    
  
