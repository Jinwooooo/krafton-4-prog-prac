import sys

val = sys.stdin.readline().replace('\n', '').split(' ')
pre = int(val[0])
post = int(val[1])

print(pre + post)
print(pre - post)
print(pre * post)
print(pre // post)
print(pre % post)
