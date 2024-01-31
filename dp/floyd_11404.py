import sys
input = sys.stdin.readline

# debugging purposes
def print_g(graph):
    for row in graph:
        print(row)

# bj output wants inf to be regarded as 0 in final SP graph
def bj_out_format(graph, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == float('inf'):
                graph[i][j] = 0

    for row in graph:
        print(*row)

def floyd(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    return graph 

# init
inf = float('inf')
n = int(input().strip())
no_in = int(input().strip())
graph = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(no_in):
    node_1, node_2, weight = map(int, input().strip().split(' '))
    # handling same start and end with different edge value
    if graph[node_1 - 1][node_2 - 1] >= weight:
        graph[node_1 - 1][node_2 - 1] = weight

for idx in range(n):
    graph[idx][idx] = 0

# main
bj_out_format(floyd(graph, n), n)
