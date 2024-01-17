import sys

n = int(sys.stdin.readline())
tower_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
stack = []
output_arr = [0 for _ in range(n)]

for idx in range(n):
	while stack:
		# if the current tower height is shorter than the stacked tower heights
		if stack[-1][1] > tower_arr[idx]:
			output_arr[idx] = stack [-1][0] + 1 # because index starts at 0, but the output req starts at 1
			break
		# if the current tower height is taller, than the prev tower heights are no longer needed (no longer has effect)
		else:
			stack.pop()
	stack.append([idx, tower_arr[idx]]) # pushing [tower index position, tower height] to stack

print(' '.join(map(str, output_arr))) 

