from dimacs import *
import os, sys, time
##### DO ZROBIENIA BISEARCH


def adjacency_list(V, L):
    adj_graph = [[] for _ in range(V)]
    weights = []
    for (x,y,c) in L:
        adj_graph[int(x-1)].append((int(y-1), int(c)))
        adj_graph[int(y-1)].append((int(x-1), int(c)))
        if c not in weights: weights.append(c)
    return weights, adj_graph


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def dfs_recursive(graph, vertex, min_weight, path):
    path.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor[0] not in path and neighbor[1] >= min_weight:
            dfs_recursive(graph, neighbor[0], min_weight, path)
    return 1 in path


def m_bottleneck(V, L):
    weights, adj_graph = adjacency_list(V, L)
    weights.sort(reverse=True)
    for min_weight in weights:
        path = []
        if dfs_recursive(adj_graph, 0, min_weight, path):
            return min_weight
    return 0


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe1\testy'
copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe1/testy/'
# list file and directories
res = os.listdir(dir_path)
for el in res:
    start = time.time()
    name = copy + el
    (V, L) = loadWeightedGraph(name)
    moja_funkcja = m_bottleneck(V, L)
    poprawny_wynik = int(readSolution(name))
    if moja_funkcja == poprawny_wynik:
        print("Wynik poprawny dla:", el)
    else:
        print("Wynik niepoprawny dla:", el, "moja funkcja:", moja_funkcja, "poprawny:", poprawny_wynik)
    end = time.time()
    print("Czas wykonania:", end - start,"s")
    print()