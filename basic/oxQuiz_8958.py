import sys
input = sys.stdin.readline

no_input = int(input().strip())
output_arr = []
incr_arr = [i for i in range(1, 81)]

for _ in range(no_input):
	str_ox = input().strip().split('X')
	score = 0
	for sub_ox in str_ox:
		score += sum(incr_arr[:len(sub_ox)])
	output_arr.append(score)

for val in output_arr:
	print(val)