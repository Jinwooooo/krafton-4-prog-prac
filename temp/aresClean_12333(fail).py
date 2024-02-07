import sys
from collections import deque
input = sys.stdin.readline

def print_room(mat):
	for row in mat:
		print(row)
	print('-------------')

def bfs_room(room_a, room_b, clean, visit, row, col, d, x, y):
	q = deque([(row, col, d)])
	direct = [[-1,0],[0,1],[1,0],[0,-1]]
	move_ctr = 0

	while q:
		# print('***********')
		row, col, d = q.popleft()
		if clean[row][col] == False:
			d = (d + room_a[row][col]) % 4
			# print('d room_a after change = ', d)
			nrow = row + direct[d][0]
			ncol = col + direct[d][1]
		else:
			# print('d room_b after change = ', d)
			d = (d + room_b[row][col]) % 4
			nrow = row + direct[d][0]
			ncol = col + direct[d][1]

		if 0 <= nrow < y and 0 <= ncol < x:

			visit[row][col] = True
			clean[row][col] = True
			move_ctr += 1
			if not visit[nrow][ncol]:
				q.append((nrow, ncol, d))
		else:
			break
		
		# print_room(clean)
		# print_room(visit)
		# print('nrow, ncol = ', nrow, ncol)
		# print('***********')

	return clean, visit, nrow, ncol, d, move_ctr

y, x = map(int, input().strip().split(' '))
row, col, d = map(int, input().strip().split(' '))

room_a = [list(map(int, input().strip())) for _ in range(y)]
room_b = [list(map(int, input().strip())) for _ in range(y)]
clean = [[False for _ in range(x)] for _ in range(y)]

visit = [[False for _ in range(x)] for _ in range(y)]
clean, visit, row, col, d, ctr = bfs_room(room_a, room_b, clean, visit, row, col, d, x, y)
print('iter 1 table')
print_room(clean)
print_room(visit)
print('row, col = ', row, col)
print(ctr)
print(d)

visit = [[False for _ in range(x)] for _ in range(y)]
clean, visit, row, col, d, ctr = bfs_room(room_a, room_b, clean, visit, row, col, d, x, y)
print('iter 2 table')
print_room(clean)
print_room(visit)
print('row, col = ', row, col)
print(ctr)
print(d)

visit = [[False for _ in range(x)] for _ in range(y)]
clean, visit, row, col, d, ctr = bfs_room(room_a, room_b, clean, visit, row, col, d, x, y)
print('iter 3 table')
print_room(clean)
print_room(visit)
print('row, col = ', row, col)
print(ctr)
print(d)

# final_ctr = 0
# for _ in range(3):
# 	visit = [[False for _ in range(x)] for _ in range(y)]
# 	prev_clean = clean[:]
# 	print_room(prev_clean)
# 	clean, visit, row, col, d, ctr = bfs_room(room_a, room_b, clean, visit, row, col, d, x, y)
# 	print_room(clean)
# 	final_ctr += ctr
# 	# if prev_clean != clean:
# 	# 	final_ctr += ctr
# 	# else:
# 	# 	print(final_ctr)
# 	# 	exit(0)
# print(final_ctr)
