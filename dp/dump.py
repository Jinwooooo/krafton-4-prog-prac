import sys
input = sys.stdin.readline
N = int(input())

t = []
p = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)


for i in range(N-1, -1, -1): # 뒤에서부터 거꾸로
    if t[i] + i > N: # 상담에 필요한 일수가 퇴사일을 넘어가면
        dp[i] = dp[i+1] # 다음날 값 그대로 가져옴
    
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i]) # 오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값

print(dp[0])
                    
# N까지 갈 수 없다면 -1, 가능하다면 최솟값 출력
# if len(dp[N]) == 0:
#     print(-1)
# else:
#     print(min(dp[N].values()))

# import sys
# from collections import deque

# N, M = map(int, sys.stdin.readline().split())
# check = [[] for _ in range(N + 1)]
# small_rock = set()
# for _ in range(M):
#     small = int(sys.stdin.readline())
#     small_rock.add(small)

# def solution(N, check, small_rock):
#     queue = deque([(1, 0, 0)])
#     while queue:
#         location, jump, n = queue.popleft()
#         for x in [jump + 1, jump, jump - 1]:
#             if x > 0:
#                 next_location = location + x
#                 if next_location == N:
#                     return n + 1
#                 if (next_location < N) and (next_location not in small_rock) and (x not in check[next_location]):
#                     check[next_location].append(x)
#                     queue.append((next_location, x, n + 1))
#         print(queue)
#     return -1 

# print(solution(N, check, small_rock))
