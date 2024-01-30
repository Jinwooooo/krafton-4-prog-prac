import sys

input = sys.stdin.readline

output_arr = []

for _ in range(int(input().strip())):
	pot_cand = []
	for _ in range(int(input().strip())):
		pot_cand.append(list(map(int, input().strip().split(' '))))
	pot_cand.sort()

	total_cand = 1
	curr_max = pot_cand[0][1] # 4
	for idx in range(1, len(pot_cand)):
		if curr_max > pot_cand[idx][1]:
			curr_max = pot_cand[idx][1]
			total_cand += 1
	output_arr.append(total_cand)

for a in output_arr:
	print(a)