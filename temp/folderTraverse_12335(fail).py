import sys
input = sys.stdin.readline

def print_g(graph):
	for row in graph:
		print(row)

no_folder, no_space = map(int, input().strip().split(' '))
graph = [[0 for _ in range(no_folder)] for _ in range (no_folder)]
for i in range(no_folder):
	curr_in = list(map(int, input().strip().split(' ')))[1:]
	for curr in curr_in:
		graph[i][curr-1] = 1
		graph[curr-1][i] = 1

print_g(graph)