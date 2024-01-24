import sys

test_total_no = int(sys.stdin.readline())

def fact(k):
	if k == 0:
		return 1
	else:
		return k * fact(k-1)

print(fact(test_total_no))