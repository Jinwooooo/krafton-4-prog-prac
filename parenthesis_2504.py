import sys

def round_brac_compute(stack, prev_val, valid_cond):
	while stack:
		curr_val = stack.pop()
		if curr_val == '(':
			if prev_val == 0:
				stack.append(2)
			else:
				stack.append(prev_val * 2)
			break
		elif type(curr_val) == int:
			if prev_val == 0:
				prev_val = curr_val
			else:
				prev_val += curr_val
		else:
			valid_cond = False

	return stack, prev_val, valid_cond

def sqr_brac_compute(stack, prev_val, valid_cond):
	while stack:
		curr_val = stack.pop()
		if curr_val == '[':
			if prev_val == 0:
				stack.append(3)
			else:
				stack.append(prev_val * 3)
			break
		elif type(curr_val) == int:
			if prev_val == 0:
				prev_val = curr_val
			else:
				prev_val += curr_val
		else:
			valid_cond = False

	return stack, prev_val, valid_cond

stack = []
arr = list(sys.stdin.readline().strip())
valid_cond = True

# if ~ elif = reduces the computing work, all 3 special cases all are included in the invalid set of mismatch bracket
# invalid special case : length = 1
if len(arr) == 1:
	valid_cond = False
# invalid special case : first bracket is closer
elif arr[0] == ')' or arr[0] == ']':
	valid_cond = False
# invalid special case : bracket is always a pair, so odd length will surely fail
elif len(arr) % 2 != 0:
	valid_cond = False
else:
	for bracket in arr:
		# invalid special case : when stack is empty, inserting closing bracket case
		if not stack:
			if bracket == ')' or bracket == ']':
				valid_cond = False
				break
			else:
				# closing bracket (i.e. need to pop from stack)
				if bracket == ')':
					prev_val = 0
					stack, prev_val, valid_cond = round_brac_compute(stack, prev_val, valid_cond)
					if valid_cond == False: break
				elif bracket == ']':
					prev_val = 0
					stack, prev_val, valid_cond = sqr_brac_compute(stack, prev_val, valid_cond)
					if valid_cond == False: break
				# opening brackets (i.e. need to push/append to stack)
				else:
					stack.append(bracket)
		else:
			# closing bracket (i.e. need to pop from stack)
			if bracket == ')':
				prev_val = 0
				stack, prev_val, valid_cond = round_brac_compute(stack, prev_val, valid_cond)
				if valid_cond == False: break
			elif bracket == ']':
				prev_val = 0
				stack, prev_val, valid_cond = sqr_brac_compute(stack, prev_val, valid_cond)
				if valid_cond == False: break
			# opening brackets (i.e. need to push/append to stack)
			else:
				stack.append(bracket)

output = 0
if valid_cond == False:
	output = 0
else:
	for val in stack:
		# invalid case : if the stack has brackets remaining case (i.e. mismatch brackets)
		if type(val) != int:
			output = 0
			break
		else:
			output += val

print(output)
