import sys
from itertools import combinations

#########################
# finding all prime val #
#########################

max_val = 10000
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

#####################################
# find sum of the lowest difference #
#####################################

prime_combinations = { sum(pair): pair for pair in combinations(prime_list, 2) }
output_list = []

test_size = int(sys.stdin.readline())

for _ in range(test_size):
    sum_val = int(sys.stdin.readline())

    if sum_val % 2 == 0:
        half_sum = sum_val // 2
        if half_sum in prime_list:
            output_list.append((half_sum, half_sum))
        else:
            output_list.append(prime_combinations[sum_val])
    else:
        output_list.append(prime_combinations[sum_val])

for record in output_list:
    print(record[0], record[1])
