from dimacs import *
import os, sys, time

# implement solution here


def adjacency_list(V, L):
    adj_graph = [[] for _ in range(V)]
    for (x,y,c) in L:
        adj_graph[x-1].append([y-1, c])
        adj_graph[y-1].append([x-1, 0])
    return adj_graph


def dfs_visit(G, V, P, i):
    V[i] = True
    for nb in G[i]:
        if not V[nb[0]] and nb[1] != 0:
            P[nb[0]] = i
            dfs_visit(G, V, P, nb[0])


def dfs(G, P, s, t):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s)
    return V[t]


def Ford_Fulk(G, s, t):
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, P, s, t):
        curr_flow = 10**9
        current = t
        while current != s: # cofanie do początku szukając bottlenecka
            parent = P[current]
            for i in range(len(G[parent])):
                if G[parent][i][0] == current:
                    curr_flow = min(curr_flow, G[parent][i][1])
                    break
            current = P[current]
        max_flow += curr_flow

        v = t
        while v != s: # uaktualnie grafu po przepływie
            u = P[v]
            for i in range(len(G[u])):
                if G[u][i][0] == v:
                    G[u][i][1] -= curr_flow
                    break
            for i in range(len(G[v])):
                if G[v][i][0] == u:
                    G[v][i][1] += curr_flow
                    break
            v = P[v]
    return max_flow



def solution(V, L):
    adj_g = adjacency_list(V, L)
    return Ford_Fulk(adj_g, 0, V-1)


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
