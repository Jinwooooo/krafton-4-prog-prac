import sys

input = sys.stdin.readline

no_input = int(input().strip())

pos_time = []
for _ in range(no_input):
	pos_time.append(list(map(int, input().strip().split(' '))))
pos_time.sort(key = lambda x: (x[1], x[0]))

max_meeting = 0
curr_end = 0
for start, end in pos_time:
	if curr_end <= start:
		curr_end = end
		max_meeting += 1

print(max_meeting)


# all_time = [0 for _ in range(10**5)]

# max_meeting = 0
# while pos_time:
# 	time, start, end = pos_time.popleft()
# 	if time == 0:
# 		max_meeting += 1
# 	elif time == 1:
# 		for i in range(start, end + 1):
# 			all_time[i] = 1
# 		max_meeting += 1
# 	else:
# 		if all_time[start + 1] != 1 and all_time[end - 1] != 1:
# 			for i in range(start, end + 1):
# 				all_time[i] = 1
# 			max_meeting += 1

# print(max_meeting)

