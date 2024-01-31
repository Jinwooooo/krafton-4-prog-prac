import sys
from heapq import heappush, heappop
input = sys.stdin.readline

no_jewels, no_bags = map(int, input().strip().split(' '))

jewel = []
for _ in range(no_jewels):
	weight, value = map(int, input().strip().split(' '))
	jewel.append((weight, value))
jewel.sort(reverse = True)
bag = sorted(int(input().strip()) for _ in range(no_bags))

bag_heap = []
total_max = []
for b in bag:

	while jewel and jewel[-1][0] <= b:
		_, value = jewel.pop()
		heappush(bag_heap, -value)

	if bag_heap:
		total_max.append(-heappop(bag_heap))
	elif not jewel:
		break

# print(total_max)
print(sum(total_max))

# while jewel and bag:
# 	curr_val, curr_weight = heappop(jewel)
# 	curr_val = -curr_val

# 	idx = bisect_left(bag, curr_weight)
# 	if idx == len(bag):
# 		if bag[-1] >= curr_weight:
# 			total_max.append(curr_weight)
# 			bag.pop()
# 	elif idx < len(bag):
# 		total_max.append(curr_val)
# 		bag.remove(bag[idx]) # this part is incredibly slow

