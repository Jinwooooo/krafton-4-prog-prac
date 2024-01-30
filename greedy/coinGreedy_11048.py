import sys

input = sys.stdin.readline

# input format
no_coin, total = map(int, input().strip().split(' '))
coin_type = []
for _ in range(no_coin):
	coin_type.append(int(input()))
total_coin = 0

# removing unneeded coins (i.e. coin value > total value)
while True:
	temp = coin_type.pop()
	# due to pop, appending the value where it is now longer divisable
	if total//temp > 0:
		coin_type.append(temp)
		break

# main : extracting amount of coins req to fufill total
total_coin = 0
while total != 0:
	curr_type = coin_type.pop()
	if total // curr_type > 0:
		sub_multiplier = total // curr_type
		total -= curr_type * sub_multiplier

		total_coin += sub_multiplier

print(total_coin)