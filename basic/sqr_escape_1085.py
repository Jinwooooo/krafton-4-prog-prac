import sys
from math import inf
input = sys.stdin.readline

x, y, w, h = map(int, input().strip().split(' '))

print(min(abs(x-0), abs(x-w), abs(y-0), abs(y-h)))
