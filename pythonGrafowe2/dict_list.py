def dict_list(V, L):
    dict_list = [{} for _ in range(V)]
    for (x,y,c) in L:
        dict_list[int(x-1)][int(y-1)] = c
        dict_list[int(y-1)][int(x-1)] = 0
    return dict_list