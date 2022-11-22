from dimacs import *
import os, sys, time
import copy

# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# On every step use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution.


def dict_list(V, L):
    dict_list = [{} for _ in range(V)]
    for (x,y,c) in L:
        dict_list[x-1][y-1] = c
        # if not int(x-1) in dict_list[int(y-1)].keys(): dict_list[int(y-1)][int(x-1)] = 0
        dict_list[y-1][x-1] = 0
    return dict_list


def dfs_visit(G, Visited, P, i):
    Visited[i] = True
    for nb in G[i]:
        if not Visited[nb] and G[i][nb] != 0:
            P[nb] = i
            dfs_visit(G, Visited, P, nb)


def dfs(G, s, t, P, V):
    Visited = [False for _ in range(V)]
    dfs_visit(G, Visited, P, s)
    return Visited[t]


def Ford_Fulk(G, s, t, V):
    P = [None for _ in range(V)]
    max_flow = 0
    while dfs(G, s, t, P, V):
        curr_flow = 10**9
        current = t
        while current != s:
            curr_flow = min(curr_flow, G[P[current]][current])
            current = P[current]
        max_flow += curr_flow
        v = t
        while v != s:
            u = P[v]
            G[u][v] -= curr_flow
            G[v][u] += curr_flow
            v = P[v]
    return max_flow


def solution(V,L):
    G = dict_list(V, L)
    maxi = 0
    # check = []
    for vertex in range(1, V):
        g_copy = copy.deepcopy(G)
        maxi = max(maxi, Ford_Fulk(g_copy, 0, vertex, V))
        # check.append(Ford_Fulk(g_copy,0,vertex,V))
    return maxi
    # return check


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe2\connectivity'
d_path_copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/connectivity/'
# list file and directories
res = os.listdir(d_path_copy)
beg = time.time()
good = 0
all = 0
for el in res:
    # if el:
    if el != "grid100x100":
        start = time.time()
        name = d_path_copy + el
        # (V, L) = loadDirectedWeightedGraph(name)
        (V, L) = loadWeightedGraph(name)
        moja_funkcja = solution(V, L)
        poprawny_wynik = int(readSolution(name))
        print("-------------------------")
        if moja_funkcja == poprawny_wynik:
            good += 1
            print("Wynik poprawny dla:", el)
        else:
            print("Wynik niepoprawny dla:", el)
            print("moja funkcja:", moja_funkcja)
            print("poprawny:", poprawny_wynik)
        all += 1

        end = time.time()
        print("Orientacyjny czas wykonania:", end - start,"s")
        print()

print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:",time.time() - beg, "s")
