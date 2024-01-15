import sys
from itertools import combinations

# [DEBUG]
# height_list = [20, 7, 23, 19, 10, 15, 25, 8, 13]

height_list = []

for _ in range(9):
	height_list.append(int(sys.stdin.readline()))

combi_dict = { sum(subset7) : subset7 for subset7 in combinations(height_list, 7) }

real_list = list(combi_dict.get(100))
real_list.sort()

for a in real_list:
	print(a)
