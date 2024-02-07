import sys
input = sys.stdin.readline

string = list(input().strip())
string.sort(reverse=True)
idx_mid = len(string) // 2 + 1
output = [''] + ['' for _ in range(len(string))]

if len(string) == 1:
	print(''.join(string))
else:
	idx_ctr = 1
	while len(string) >= 2:
		char_1 = string.pop()
		char_2 = string.pop()

		if char_1 == char_2:
			output[idx_ctr] = char_1
			output[-idx_ctr] = char_2
			idx_ctr += 1
		else:
			# if the string is even, one bullet is left in the chamber
			if len(string) % 2 == 1:
				char_3 = string.pop()
				if char_2 == char_3:
					output[idx_ctr] = char_2
					output[-idx_ctr] = char_3
					idx_ctr += 1
					output[idx_mid] = char_1
				else:
					print("I'm Sorry Hansoo")
					exit(0)
			else:
				print("I'm Sorry Hansoo")
				exit(0)

		if len(string) == 1:
			output[idx_mid] = string.pop()

	print(''.join(output))
