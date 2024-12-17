def shortest_path(n, edges):
    d = [[float('inf')] * n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        d[u - 1][v - 1] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] != float('inf') and d[k][j] != float('inf'):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if d[i][j] == float('inf'):
                row.append(-1)
            else:
                row.append(d[i][j])
        result.append(" ".join(map(str, row)))
    
    return "\n".join(result)
    
n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    
print(shortest_path(n, edges))
