import sys

#########################
# finding all prime val #
#########################
max_val = 1000
is_prime = [1] * max_val
is_prime[0] = 0
is_prime[1] = 0

def sieve_of_eratosthenes():
	curr_val = 2

	while curr_val * curr_val <= max_val:
		if is_prime[curr_val] == 0:
			curr_val += 1
			continue

		comp_val = 2 * curr_val
		while comp_val < max_val:
			is_prime[comp_val] = 0
			comp_val += curr_val

		curr_val += 1

sieve_of_eratosthenes()

prime_list = []
for chk_val in range(1, max_val):
    if is_prime[chk_val] == 1:
    	prime_list.append(chk_val)

####################################
# compare prime list and test list #
####################################

test_size = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))

print(len(set(prime_list) & set(input_list)))



