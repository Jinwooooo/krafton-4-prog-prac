import sys
input = sys.stdin.readline

no_user = int(input().strip())
time_arr = list(map(int, input().strip().split(' ')))
time_arr.sort()

user_time = [time_arr[0]]
for idx in range(1, len(time_arr)):
	user_time.append(user_time[idx - 1] + time_arr[idx])

print(sum(user_time))
