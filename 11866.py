import sys

# system input
in_tuple = list(map(int, sys.stdin.readline().split(' ')))
curr_arr = []
out_arr = []

# creating circular list
for i in range(in_tuple[0]):
	curr_arr.append(i+1)

list_size = in_tuple[0]
kill_skip = in_tuple[1] - 1
curr_index = 0

for _ in range(in_tuple[0]):
# special case when there is only 1 value left
	if list_size == 1:
		out_arr.append(curr_arr[0])
	# special case when there is only 2 values left
	elif list_size == 2:
		out_arr.append(curr_arr[1])
		list_size -= 1
	# general case
	else:
		kill_arr = curr_arr[1:]
		killer_val = curr_arr[0]

		# if the skip var goes over the list size
		kill_skip_mod =  kill_skip % (list_size - 1)
		if kill_skip_mod == 0:
			kill_skip_mod = list_size - 2
			kill_val = kill_arr[kill_skip_mod]
			curr_arr = kill_arr[:kill_skip_mod] + [killer_val]
			# print("[DEBUG] IN kill_skip_mod == 0 ; kill_val = ", kill_val)
		else:
			kill_skip_mod -= 1
			kill_val = kill_arr[kill_skip_mod]
			curr_arr = kill_arr[(kill_skip_mod + 1):] + [killer_val] + kill_arr[:kill_skip_mod]
			# print("[DEBUG] IN kill_skip_mod != 0; kill_val = ", kill_val)

		list_size -= 1
		out_arr.append(kill_val)
		# print("[DEBUG] after_arr = ", curr_arr)
		# print("-------------------------------")

out_arr = ', '.join(list(map(str, out_arr)))
print('<' + out_arr + '>')
