def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n
    mst_weight = 0
    
    edges.sort(key=lambda x: x[2])
    
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += w
            
    return mst_weight

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges = [(u-1, v-1, w) for u, v, w in edges]  
    print(kruskal(N, edges))

if __name__ == "__main__":
    main()
