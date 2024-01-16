import sys
from collections import deque

stack = deque()
post_addition_arr = []
final_addition_arr = []

# test1 = list('(()[[]])([])') # 28
# test2 = list('[][]((])') # 0
# test3 = list('(()[[]])') # 22

arr = deque(list(sys.stdin.readline().strip()))

if len(arr) == 1:
	output = 0
elif arr[0] == ')' or arr[0] == ']':
	output = 0
else:
	temp_holder = 0
	stack.append(arr.popleft())
	prev_op = "push"
	for bracket in arr:
		if len(stack) > 1:
			if bracket == '(':
				# print('[debug] in ', chr(40))
				if prev_op == "pop":
					post_addition_arr.append(temp_holder)
					prev_op = "push"
					stack.append(bracket)
				else:
					stack.append(bracket)
			elif bracket == '[':
				# print('[debug] in ', chr(91))
				if prev_op == "pop":
					post_addition_arr.append(temp_holder)
					prev_op = "push"
					stack.append(bracket)
				else:
					stack.append(bracket)
			elif bracket == ')':
				curr_brac = stack.pop()
				if curr_brac == '(':
					if prev_op == "pop":
						temp_holder *= 2
						# print('[debug] in if', chr(41), 'nest, temp_holder = ', temp_holder)
					else:
						temp_holder = 2
						# print('[debug] in if', chr(41), 'init, temp_holder = ', temp_holder)
						prev_op = "pop"
				else:
					# fail case, parenthese does not match
					output = 0
					break
			elif bracket == ']':
				curr_brac = stack.pop()
				if curr_brac == '[':
					if prev_op == "pop":
						temp_holder *= 3
						# print('[debug] in if', chr(93), 'nest, temp_holder = ', temp_holder)
					else:
						temp_holder = 3
						# print('[debug] in if', chr(93), 'init, temp_holder = ', temp_holder)
						prev_op = "pop"
				else:
					# fail case, parenthese does not match
					output = 0
					break
		else:
			if bracket == '(':
				if prev_op == "pop":
					post_addition_arr.append(temp_holder)
					prev_op = "push"
					stack.append(bracket)
				else:
					stack.append(bracket)
			elif bracket == '[':
				if prev_op == "pop":
					post_addition_arr.append(temp_holder)
					prev_op = "push"
					stack.append(bracket)
				else:
					stack.append(bracket)
			elif bracket == ')':
				curr_brac = stack.pop()
				if curr_brac == '(':
					if prev_op == "pop":
						post_addition_arr.append(temp_holder)
						final_addition_arr.append(sum(post_addition_arr) * 2)
						post_addition_arr = []
						temp_holder = 0
						# print('[debug] in else', chr(41), 'nest, temp_holder = ', temp_holder)
					else:
						temp_holder = 2
						# print('[debug] in else', chr(41), 'init, temp_holder = ', temp_holder)
						prev_op = "pop"
				else:
					# fail case, parenthese does not match
					output = 0
					break
			elif bracket == ']':
				curr_brac = stack.pop()
				if curr_brac == '[':
					if prev_op == "pop":
						post_addition_arr.append(temp_holder)
						final_addition_arr.append(sum(post_addition_arr) * 3)
						post_addition_arr = []
						temp_holder = 0
						# print('[debug] in else', chr(93), 'nest, temp_holder = ', temp_holder)
					else:
						temp_holder = 3
						# print('[debug] in else', chr(93), 'init, temp_holder = ', temp_holder)
						prev_op = "pop"
				else:
					# fail case, parenthese does not match
					output = 0
					break

print(sum(final_addition_arr))
