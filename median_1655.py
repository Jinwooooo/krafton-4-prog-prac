import sys
from heapq import heappop, heappush, heapify

def find_median():
	if not min_heap:
		return -max_heap[0]
	elif -max_heap[0] < min_heap[0]:
		return -max_heap[0]
	elif -max_heap[0] > min_heap[0]:
		return min_heap[0]
	else:
		return min_heap[0]

in_no = int(sys.stdin.readline())
out_arr = []
max_heap = []
min_heap = []
heapify(max_heap)
heapify(min_heap)

for _ in range(in_no):
	in_val = int(sys.stdin.readline())

	if len(max_heap) == len(min_heap):
		heappush(max_heap, -in_val)
	else:
		heappush(min_heap, in_val)

	if min_heap and -max_heap[0] > min_heap[0]:
		temp_min = heappop(min_heap)
		temp_max = heappop(max_heap)
		heappush(max_heap, -temp_min)
		heappush(min_heap, -temp_max)

	out_arr.append(find_median())

for a in out_arr:
	print(a)
