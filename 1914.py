import sys

stacks = int(sys.stdin.readline())

def tower_of_hanoi_total_moves(k):
	return 2**k - 1

def tower_of_hanoi_move_list(k, source, temp, target):
	if k == 1:
		print(source, target)
	else:
		tower_of_hanoi_move_list(k-1, source, target, temp)
		print(source, target)
		tower_of_hanoi_move_list(k-1, temp, source, target)

print(tower_of_hanoi_total_moves(stacks))
if stacks < 21:
	tower_of_hanoi_move_list(stacks, 1, 2, 3)

