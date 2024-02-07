
# def subset_sum_recursive(nums, target_sum):

#     def backtrack(start, current_subset, current_sum):
#         nonlocal val
#         if current_sum == target_sum:
#             if len(current_subset) != 1:
#                 val += 1
#                 result.append(current_subset[:])  # Add a copy of the subset to the result

#         for i in range(start, len(nums)):
#             current_sum += nums[i]
#             current_subset.append(nums[i])

#             # Recur with the next element and the updated subset and sum
#             backtrack(i + 1, current_subset, current_sum)

#             # Backtrack by removing the last element
#             current_subset.pop()
#             current_sum -= nums[i]

#     result = []
#     val = 0
#     nums.sort()  # Sorting the array can help with pruning and duplicate avoidance
#     backtrack(0, [], 0)

#     return result, val

# # Example usage:
# numbers = [-7, -3, -2, 5, 8]
# target = 0
# result, val = subset_sum_recursive(numbers, target)

# print(val)
# for subset in result:
#     print(f"Subset: {subset}, Sum: {sum(subset)}")


# bracket = input()
# length = len(bracket)
# stack = []
# tmp = 1
# res = 0

# for i in range(length):
#     b = bracket[i]   
#     if b == '(':
#         tmp *= 2
#         print(stack)
#         stack.append(b)
#     elif b == '[':
#         tmp *= 3
#         print(stack)
#         stack.append(b)
#     elif b == ')':
#         if not stack or stack[-1] == '[':
#             res = 0
#             break
#         if bracket[i-1] == '(':
#             res += tmp
#         tmp //= 2
#         print(stack)
#         stack.pop()  
#     else:
#         if not stack or stack[-1] == '(':
#             res = 0
#             break
#         if bracket[i-1] == '[':
#             res += tmp
#         tmp //= 3
#         print(stack)
#         stack.pop() 

# if stack:
#     res = 0
# print(res)


# string = input()
# stack = []

# for char in string:
#     if char == ')':
#         temp = 0
#         while stack:
#             print('in ) debug', stack)
#             top = stack.pop()
#             if top == '(':
#                 if temp == 0:
#                     stack.append(2)
#                 else:
#                     stack.append(temp*2)
#                 break
#             elif type(top) == int:
#                 if temp == 0:
#                     temp = int(top)
#                 else:
#                     temp += int(top)
#             else:
#                 print(0)
#                 exit(0)
    
#     elif char == ']':
#         temp = 0
#         while stack:
#             print('in ] debug', stack)
#             top = stack.pop()
#             if top == '[':
#                 if temp == 0:
#                     stack.append(3)
#                 else:
#                     stack.append(temp*3)
#                 break
#             elif type(top) == int:
#                 if temp == 0:
#                     temp = int(top)
#                 else:
#                     temp += int(top)
#             else:
#                 print(0)
#                 exit(0)
    
#     else:
#         stack.append(char)

# result = 0
# for char in stack:
#     if type(char) != int:
#         break
#     else:
#         result += char

# print(result)


# if len(arr) == 1:
# 	output = 0
# elif arr[0] == ')' or arr[0] == ']':
# 	output = 0
# else:
# 	temp_holder = 0
# 	stack.append(arr.popleft())
# 	prev_op = "push"
# 	for bracket in arr:
# 		if len(stack) > 1:
# 			if bracket == '(':
# 				# print('[debug] in ', chr(40))
# 				if prev_op == "pop":
# 					post_addition_arr.append(temp_holder)
# 					prev_op = "push"
# 					stack.append(bracket)
# 				else:
# 					stack.append(bracket)
# 			elif bracket == '[':
# 				# print('[debug] in ', chr(91))
# 				if prev_op == "pop":
# 					post_addition_arr.append(temp_holder)
# 					prev_op = "push"
# 					stack.append(bracket)
# 				else:
# 					stack.append(bracket)
# 			elif bracket == ')':
# 				curr_brac = stack.pop()
# 				if curr_brac == '(':
# 					if prev_op == "pop":
# 						temp_holder *= 2
# 						# print('[debug] in if', chr(41), 'nest, temp_holder = ', temp_holder)
# 					else:
# 						temp_holder = 2
# 						# print('[debug] in if', chr(41), 'init, temp_holder = ', temp_holder)
# 						prev_op = "pop"
# 				else:
# 					# fail case, parenthese does not match
# 					output = 0
# 					break
# 			elif bracket == ']':
# 				curr_brac = stack.pop()
# 				if curr_brac == '[':
# 					if prev_op == "pop":
# 						temp_holder *= 3
# 						# print('[debug] in if', chr(93), 'nest, temp_holder = ', temp_holder)
# 					else:
# 						temp_holder = 3
# 						# print('[debug] in if', chr(93), 'init, temp_holder = ', temp_holder)
# 						prev_op = "pop"
# 				else:
# 					# fail case, parenthese does not match
# 					output = 0
# 					break
# 			else:
# 				# invalid input
# 				output = 0
# 				break
# 		else:
# 			if bracket == '(':
# 				if prev_op == "pop":
# 					post_addition_arr.append(temp_holder)
# 					prev_op = "push"
# 					stack.append(bracket)
# 				else:
# 					stack.append(bracket)
# 			elif bracket == '[':
# 				if prev_op == "pop":
# 					post_addition_arr.append(temp_holder)
# 					prev_op = "push"
# 					stack.append(bracket)
# 				else:
# 					stack.append(bracket)
# 			elif bracket == ')':
# 				curr_brac = stack.pop()
# 				if curr_brac == '(':
# 					if prev_op == "pop":
# 						post_addition_arr.append(temp_holder)
# 						final_addition_arr.append(sum(post_addition_arr) * 2)
# 						post_addition_arr = []
# 						temp_holder = 0
# 						# print('[debug] in else', chr(41), 'nest, temp_holder = ', temp_holder)
# 					else:
# 						temp_holder = 2
# 						# print('[debug] in else', chr(41), 'init, temp_holder = ', temp_holder)
# 						prev_op = "pop"
# 				else:
# 					# fail case, parenthese does not match
# 					output = 0
# 					break
# 			elif bracket == ']':
# 				curr_brac = stack.pop()
# 				if curr_brac == '[':
# 					if prev_op == "pop":
# 						post_addition_arr.append(temp_holder)
# 						final_addition_arr.append(sum(post_addition_arr) * 3)
# 						post_addition_arr = []
# 						temp_holder = 0
# 						# print('[debug] in else', chr(93), 'nest, temp_holder = ', temp_holder)
# 					else:
# 						temp_holder = 3
# 						# print('[debug] in else', chr(93), 'init, temp_holder = ', temp_holder)
# 						prev_op = "pop"
# 				else:
# 					# fail case, parenthese does not match
# 					output = 0
# 					break
# 			# invalid input
# 			else:
# 				output = 0
# 				break

# if len(stack) > 1:
# 	output = 0
# else:
# 	print(sum(final_addition_arr))


# import sys

# def prettify(mat):
# 	for row in mat:
# 		print(row)

# def create_board(n):
# 	board = []
# 	for _ in range(n):
# 	    row = []
# 	    for _ in range(n):
# 	        row.append(0)
# 	    board.append(row)

# 	return board

# def place_piece(board, n, pos):
# 	x, y = pos
# 	board[x][y] = -1

# 	return board

# def chk_validity(board, n, pos):
# 	x, y = pos

# 	# vertical
# 	for i in range(n):
# 		if board[x][i] == -1:
# 			return False

# 	# LU diag
# 	for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
# 		if board[i][j] == -1:
# 			return False

# 	# RU diag
# 	for i, j in zip(range(x, -1, -1), range(y, n, 1)):
# 		if board[i][j] == -1:
# 			return False

# 	# # vertical
# 	# for i in range(n):
# 	# 	if board[x][i] == -1:
# 	# 		return False

# 	# # LU diag
# 	# for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
# 	# 	if board[i][j] == -1:
# 	# 		return False

# 	# # LL diag
# 	# for i, j in zip(range(x, n, 1), range(y, -1, -1)):
# 	# 	if board[i][j] == -1:
# 	# 		return False

# 	return True


# n = 4
# pos = [0,0]
# board = create_board(n)

# print(chk_validity(board, n, pos))

# p2_arr = []
# for i in range(n):
# 	for j in range(n):
# 		p2_arr.append([i,j])

# for _ in range(n*n):
# 	for p2_tup in p2_arr:
# 		if(chk_validity(board, n, p2_tup) == True):
# 			place_piece(board, n, p2_tup)

# 	print('--------------')
# 	prettify(board)

# 	if sum(sum(board,[])) == -n:
# 		succ_place += 1

# 	board = create_board(n)
# 	p2_arr = p2_arr[1:]

# print(succ_place)

# temp_pos_s = [[0,0], [1,0], [1,1], [1,2], [2,0], [2,1], [3,0], [3,1], [3,2], [3,3]]
# temp_pos_s = [[0,1], [1,0], [1,1], [1,2], [1,3], [2,0], [3,0], [3,1], [3,2]]

# for temp_pos in temp_pos_s:
# 	if (chk_validity(board, n, temp_pos) == True):
# 		print("--- ... marking board ... ---")
# 		place_piece(board, n, temp_pos)
# 	else:
# 		print("--- ! ---")
# 		print("cannot place object in ", temp_pos, " position")
# 		print("--- ! ---")

# 	prettify(board)




# def chk_vert_validity(board, n, pos):
# 	x, y = pos

# 	# vertical
# 	for i in range(n):
# 		if board[i][y] == -1:
# 			return False

# 	return True

# def chk_hori_validity(board, n, pos):
# 	x, y = pos

# 	# horizontal
# 	for j in range(n):
# 		if board[x][j] == -1:
# 			return False

# 	return True

# def chk_diag_validity(board, n, pos):
# 	x, y = pos

# 	# LU
# 	for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
# 		print(i, j)
# 		if board[i][j] == -1:
# 			return False

# 	# RU
# 	for i, j in zip(range(x, -1, -1), range(y, n, 1)):
# 		print(i, j)
# 		if board[i][j] == -1:
# 			return False

# 	# LL
# 	for i, j in zip(range(x, n, 1), range(y, -1, -1)):
# 		print(i, j)
# 		if board[i][j] == -1:
# 			return False

# 	# RL
# 	for i, j in zip(range(x, n, 1), range(y, n, 1)):
# 		if board[i][j] == -1:
# 			return False

# 	return True