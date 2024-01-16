import sys
from collections import deque

queue = deque()
output_arr = []

for _ in range(0, int(sys.stdin.readline())):
	temp_in = sys.stdin.readline()
	# push
	if temp_in[1] == 'u':
		val = int(temp_in.strip().split(' ')[1])
		queue.append(val)
	else:
		cmd = temp_in.strip()
		if cmd == 'pop':
			if queue:
				output_arr.append(queue.popleft())
			else:
				output_arr.append(-1)
		elif cmd == 'size':
			output_arr.append(len(queue))
		elif cmd == 'empty':
			if queue:
				output_arr.append(0)
			else:
				output_arr.append(1)
		elif cmd == 'front':
			if queue:
				output_arr.append(queue[0])
			else:
				output_arr.append(-1)
		elif cmd == 'back':
			if queue:
				output_arr.append(queue[-1])
			else:
				output_arr.append(-1)
			
for a in output_arr:
	print(a)
