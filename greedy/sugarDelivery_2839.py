import sys
input = sys.stdin.readline

total = int(input().strip())
curr_5 = total // 5
bags = 0

for _ in range(2000):
	leftover = total - (5 * curr_5)

	if curr_5 < 0:
		bags = -1
		break

	if leftover % 3 == 0:
		bags = curr_5 + (leftover // 3)
		break
	else:
		curr_5 -= 1

print(bags)