from itertools import permutations

with open('data/input') as f:
    numbers = f.read().splitlines()
numbers = list(map(int, numbers))
target = 2020

solutions = [pair for pair in permutations(numbers, 2) if sum(pair) == target]
print('Solution 1:', solutions[0][0] * solutions[0][1])
