import sys

test_total_no = int(sys.stdin.readline())
output_list = []

for test_no in range(0, test_total_no):
	max_list = [''] * 8000
	input_list = sys.stdin.readline().replace('\n', '').split(' ')

	rep = int(input_list[0])
	char_list = list(input_list[1])

	for j in char_list:
		for i in range(0,rep):
			max_list.append(j)

	output_list.append(''.join(max_list))

for output in output_list:
	print(output)
