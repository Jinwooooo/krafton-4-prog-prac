import sys

input = sys.stdin.readline

# debugging purposes
def print_m(mat):
    for row in mat:
        print(row)
    print('-----------------------')

word_1 = input().strip()
word_2 = input().strip()

# row = word 1 ; col = word 2
dp = [[0 for _ in range(len(word_1) + 1)] for _ in range(len(word_2) + 1)]

for w2 in range(1, len(word_2) + 1):
    for w1 in range(1, len(word_1) + 1):
        # if same character found, increment matrix from upper left diag ctr
        if word_1[w1 - 1] == word_2[w2 - 1]:
            dp[w2][w1] = dp[w2 - 1][w1 - 1] + 1
        # else if different get max val from either left or upper cell
        else:
            dp[w2][w1] = max(dp[w2][w1 - 1], dp[w2 - 1][w1])
    print_m(dp)

# Retrieve the longest subsequence string
subsequence = ''
w2 = len(word_2)
w1 = len(word_1)

while w2 > 0 and w1 > 0:
    # go diagional
    if word_1[w1 - 1] == word_2[w2 - 1]:
        subsequence = word_1[w1 - 1] + subsequence
        w2 -= 1
        w1 -= 1
    # go up or go left
    elif dp[w2][w1] == dp[w2][w1 - 1]:
        w1 -= 1
    else:
        w2 -= 1

print('longest subsequence length = ', len(subsequence))
print('longest subsequence string = ', subsequence)

