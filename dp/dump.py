import sys

input = sys.stdin.readline

def print_m(mat):
    for row in mat:
        print(row)
    print('-----------------------')

no_ks, w_ks = map(int, input().strip().split(' '))
ks = [(0,0)]
for _ in range(no_ks):
    w, n = map(int, input().strip().split(' '))
    ks.append((w, n))

dp = [[0 for _ in range(no_ks + 1)] for _ in range(w_ks + 1)]

for w in range(1, w_ks + 1):
    for n in range(1, no_ks + 1):
        print('current weight = ', ks[n][0], ', current gain = ', ks[n][1])
        print('iteration x(w), y(n) = ', w, ',', n)
        # ks[n][0] = current weight of the item
        if w < ks[n][0]:
            # retrieve the gain from left (i.e. (n = k) == (n = k+1))
            print('weight cannot be inserted')
            dp[w][n] = dp[w][n - 1]
        else:
            print('weight can be inserted, update gain if necessary')
            print('previous gain: dp[w][n - 1] = ', dp[w][n - 1])
            print('updated gain: dp[dp[w - ks[n][0]][n - 1] + ks[n][1] = ', dp[w - ks[n][0]][n - 1] + ks[n][1])
            # update the gain if the item can be inserted
            # dp[w][n - 1] = previous max gain (i.e. n = k)
            # dp[w - ks[n][0]][n - 1] + ks[n][1] = if current weight can be inserted + insert gain
            #   dp[w - ks[n][0]] = remaining weight
            dp[w][n] = max(dp[w][n - 1], dp[w - ks[n][0]][n - 1] + ks[n][1])
        print_m(dp)
