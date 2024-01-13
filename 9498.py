import sys

def grade(val):
	if val < 60:
		print('F')
	elif val < 70:
		print('D')
	elif val < 80:
		print('C')
	elif val < 90:
		print('B')
	else:
		print('A')

grade(int(sys.stdin.readline().replace('\n', '')))
