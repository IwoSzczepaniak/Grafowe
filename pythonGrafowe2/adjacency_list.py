def adjacency_list(V, L):
    adj_graph = [[] for _ in range(V)]
    for (x,y,c) in L:
        adj_graph[x-1].append([y-1, c])
        adj_graph[y-1].append([x-1, 0])
    return adj_graph