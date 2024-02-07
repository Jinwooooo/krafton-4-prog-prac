import sys
input = sys.stdin.readline

diff_arr = []
for _ in range(int(input().strip())):
	no_log = int(input().strip())
	log = list(map(int, input().strip().split(' ')))
	log.sort(reverse = True)
	order = [-1 for _ in range(no_log + 1)]

	idx_ctr = 1
	while len(log) >= 2:
		order[idx_ctr] = log.pop()
		order[-idx_ctr] = log.pop()
		idx_ctr += 1

	if len(log) == 1:
		order[idx_ctr] = log.pop()

	max_diff = abs(order[1] - order[-1])
	for idx in range(1, no_log):
		new_diff = abs(order[idx] - order[idx + 1])
		if max_diff < new_diff:
			max_diff = new_diff

	diff_arr.append(max_diff)

for diff in diff_arr:
	print(diff)
