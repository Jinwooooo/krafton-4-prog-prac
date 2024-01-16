import sys

def gugudan(val):
	for i in range(1,10):
		eq_pre = str(val) + " * "+ str(i) +" = "
		eq_post = str(val * i)

		print(eq_pre + eq_post)

gugudan(int(sys.stdin.readline().replace('\n', '')))
