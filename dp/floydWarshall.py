import sys

def floyd_warshall(graph, n):
    d_graph = graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d_graph[i][j] = min(d_graph[i][j], d_graph[i][k] + d_graph[k][j])
    
    for row in d_graph:
        print(row)

inf = float('inf')
graph = [[0, 3, inf, 5],
        [2, 0, inf, 4],
        [inf, 1, 0, inf],
        [inf, inf, 2, 0]]
n = 4

floyd_warshall(graph, n)

