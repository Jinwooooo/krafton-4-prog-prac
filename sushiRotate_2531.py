import sys
input = sys.stdin.readline

no_dish, no_branch, cont, coupon = map(int, input().strip().split(' '))
sushi = [int(input().strip()) for _ in range(no_dish)]
lp = 0
final_seq_len = 1

# answer referenced online for optimization
# very slow as the O(n*k) + multiple O(n) is used
# only works when running on PyPy
while lp != no_dish:
	rp = lp + cont
	seq = set()
	extra = 1
	for idx in range(lp, rp):
		idx %= no_dish
		seq.add(sushi[idx])
		if sushi[idx] == coupon:
			extra = 0

	curr_seq_len = len(seq) + extra
	final_seq_len = max(final_seq_len, curr_seq_len)
	lp += 1

print(final_seq_len)

# optimized sliding window algorithm (study)
# def Input():
#     readl = sys.stdin.readline
#     N, d, k, c = map(int, readl().split())
#     dish = [ int(readl()) for _ in range(N) ]
#     return N, d, k, c, dish

# def Solve(N, d, k, c, dish):
#     dish_list = dish + dish
#     sol = -1
#     # initialize
#     visited = [0 for _ in range(d+1)]
#     visited[c] = 1
#     cnt = 1
#     tmp_cnt = 0

#     for d in dish:
#         if visited[d] == 0: 
#             cnt += 1
#             visited[d] += 1

#         else: visited[d] += 1
#         tmp_cnt += 1
#         if tmp_cnt == k: break
#     sol = max(cnt, sol)

#     for i in range(0, N):

#         # i가 start index
#         start, end = i, i+k
#         # i-1은 빠지고, end index가 들어오게 된다

#         visited[dish_list[start]] -= 1
#         if visited[dish_list[start]] == 0: cnt -= 1 # 만약 해당 index가 빠진 후 visited가 0이 된다면 가짓수 하나가 빠진다.
 
#         visited[dish_list[end]] += 1
#         if visited[dish_list[end]] == 1: cnt += 1 # 만약 해당 index가 들어온 후 visited가 1이 된다면 새로운 가짓수가 추가되는 것이므로 cnt + 1

#         sol = max(cnt, sol)

    
#     return sol

# N, d, k, c, dish = Input()
# sol = Solve(N, d, k, c, dish)
# print(sol)


# first try (time limit exceed)
# while lp != no_dish:
# 	rp = lp + cont
# 	pre = set()
# 	seq = set()
# 	post = set()
# 	for idx in range(lp, rp):
# 		idx %= no_dish
# 		seq.add(sushi[idx])
# 		if sushi[idx] == coupon:
# 			for i in range(lp - 1, rp - 1):
# 				i %= no_dish
# 				if sushi[i] != coupon:
# 					pre.add(sushi[i])
# 			for j in range(lp + 1, rp + 1):
# 				j %= no_dish
# 				if sushi[j] != coupon:
# 					post.add(sushi[j])

# 			if len(pre) == cont or len(post) == cont:
# 				seq.add(-1)

# 	curr_seq_len = len(seq)
# 	final_seq_len = max(final_seq_len, curr_seq_len)
# 	lp += 1

# print(final_seq_len)
