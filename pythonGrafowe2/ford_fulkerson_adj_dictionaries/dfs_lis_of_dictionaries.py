from dimacs import *
import os, sys, time


def dict_list(V, L):
    dict_list = [{} for _ in range(V)]
    for (x,y,c) in L:
        dict_list[int(x-1)][int(y-1)] = c
        dict_list[int(y-1)][int(x-1)] = 0
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


def solution(V, L):
    G = dict_list(V, L)
    return Ford_Fulk(G, 0, V-1, V)


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
# dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe2\flow'
dir_path = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/flow/'
# list file and directories
res = os.listdir(dir_path)
beg = time.time()
good = 0
all = 0
for el in res:
    start = time.time()
    name = dir_path + el
    (V, L) = loadDirectedWeightedGraph(name)

    moja_funkcja = solution(V, L)
    poprawny_wynik = int(readSolution(name))
    print()
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
    print("-------------------------")
    print()

        
print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:",time.time() - beg)
