def matrix_graph(V, L):
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    for (x,y,c) in L:
        matrix[x-1][y-1] = c
    return matrix