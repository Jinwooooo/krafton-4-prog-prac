import sys

input = sys.stdin.readline

# debugging purposes
def print_m(mat):
    for row in mat:
        print(row)
    print('-----------------------')

output_arr = []

for _ in range(int(input())):
    no_coin = int(input())
    type_coin = list(map(int, input().strip().split(' ')))
    total = int(input())

    # row = coin type ; col = total value
    dp = [[0 for _ in range(total + 1)] for _ in range(no_coin + 1)]
    # dp[row][0] = initial case = 1 (i.e. n = 1)
    for row in range(no_coin + 1):
        dp[row][0] = 1

    for row in range(1, no_coin + 1):
        for col in range(1, total + 1):
            # updating previous iteration possible combination values
            dp[row][col] = dp[row - 1][col]
            # if total value is lower than coin value, skip
            if type_coin[row - 1] <= col:
                dp[row][col] += dp[row][col - type_coin[row-1]]

    output_arr.append(dp[no_coin][total])

for output in output_arr:
    print(output)
