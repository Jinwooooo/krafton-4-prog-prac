import sys
from heapq import heappush, heappop
input = sys.stdin.readline

no_cards = int(input().strip())
cards_heap = []
for _ in range(no_cards):
	heappush(cards_heap, int(input().strip()))

comp = 0
while len(cards_heap) >= 2:
	min_1 = heappop(cards_heap)
	min_2 = heappop(cards_heap)
	temp_sum = min_1 + min_2
	heappush(cards_heap, temp_sum)
	comp += temp_sum

print(comp)
