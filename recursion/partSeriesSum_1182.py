import sys

n, s = map(int, sys.stdin.readline().strip().split(' '))
arr = list(map(int, sys.stdin.readline().strip().split(' ')))
subset_ctr = 0

def subset_sum(idx, sub_sum):
    global subset_ctr

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        subset_ctr += 1
    
    # arr[idx] used branch
    subset_sum(idx+1, sub_sum)
    # arr[idx] unused branch
    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0, 0)
print(subset_ctr)