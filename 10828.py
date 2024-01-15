import sys

stack = []
output_arr = []

for _ in range(0, int(sys.stdin.readline())):
	temp_in = sys.stdin.readline()
	# push
	if temp_in[1] == 'u':
		val = int(temp_in.strip().split(' ')[1])
		stack.append(val)
	else:
		cmd = temp_in.strip()
		if cmd == 'pop':
			if stack:
				output_arr.append(stack.pop())
			else:
				output_arr.append(-1)
		elif cmd == 'size':
			output_arr.append(len(stack))
		elif cmd == 'empty':
			if stack:
				output_arr.append(0)
			else:
				output_arr.append(1)
		elif cmd == 'top':
			if stack:
				output_arr.append(stack[len(stack)-1])
			else:
				output_arr.append(-1)
	
for a in output_arr:
	print(a)
