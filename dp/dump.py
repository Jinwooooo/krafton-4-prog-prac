import sys

inp = sys.stdin.readline
x = int(inp())
output = {0:0, 1:0, 2:1, 3:1}

def fnc(x):
    print(x)
    if x in output.keys():
        return output[x]
    if x % 6 == 0:
        output[x] = min(fnc(x // 3), fnc(x // 2)) + 1
    elif x % 3 == 0:
        output[x] = min(fnc(x // 3), fnc(x-1)) + 1
    elif x % 2 == 0:
        output[x] = min(fnc(x // 2), fnc(x-1)) + 1
    else:
        output[x] = fnc(x - 1) + 1
    return output[x]
test = fnc(x)
print(test)
                    
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
