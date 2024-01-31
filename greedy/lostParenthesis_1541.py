import sys

input = sys.stdin.readline

# adding '-' at the end to make sure last su
eq = input().strip() + '-'
eq_split = []

# input format
temp_c = ''
for c in eq:
	if c == '-' or c == '+':
		eq_split.append(int(temp_c))
		eq_split.append(c)
		temp_c = ''
	else:
		temp_c += c


output_arr = []
# special case, there is no subtract
if '-' not in eq_split:
	for val in eq_split:
		if type(val) == int:
			output_arr.append()
else:
	while '-' in eq_split:
		# splitting list based on '-' index location
		idx_sub = eq_split.index('-')
		eq_left = eq_split[:idx_sub]
		eq_split = eq_split[idx_sub + 1:]
		
		# adding all values before meeting another '-'
		val_temp = 0
		for val_left in eq_left:
			if type(val_left) == int:
				val_temp += val_left
		output_arr.append(-val_temp)

output_arr[0] = output_arr[0] * -1
print(sum(output_arr))


# short version
eq = input().strip().split('-')

output = sum(map(int, eq[0].split('+')))
if eq[1:]:
	for eq_sub in eq[1:]:
		val_sub = sum(map(int, eq_sub.split('+')))
		output -= val_sub

print(output)

