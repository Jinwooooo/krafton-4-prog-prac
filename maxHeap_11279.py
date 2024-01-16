import sys
from heapq import heappop, heappush, heapify

heap = []
out_arr = []
heapify(heap)

input_case = int(sys.stdin.readline())

for _ in range(input_case):
    in_val = int(sys.stdin.readline())

    if in_val == 0:
        if not heap:
            out_arr.append(0)
        else:
            out_arr.append(-1 * heappop(heap))
    else:
        heappush(heap, -1 * in_val)

for a in out_arr:
    print(a)
