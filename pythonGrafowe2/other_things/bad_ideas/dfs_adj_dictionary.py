from dimacs import *
import os, sys, time

# implement solution here





# def dfs_visit(G, Visited, P, i):
#     Visited[i] = True
#     for nb in G[i]:
#         if not Visited[nb[0]] and nb[1] != 0:
#             P[nb[0]] = i
#             dfs_visit(G, Visited, P, nb[0])
#
#
# def dfs(G, P, s, t):
#     Visited = [False for _ in range(len(G))]
#     dfs_visit(G, Visited, P, s)
#     return Visited[t]
#
# def Ford_Fulk(G, s, t):
#     P = [None for _ in range(len(G))]
#     max_flow = 0
#     while dfs(G, P, s, t):
#         curr_flow = 10**9
#         current = t
#         while current != s: # cofanie do początku szukając bottlenecka
#             parent = P[current]
#             for i in range(len(G[parent])):
#                 if G[parent][i][0] == current:
#                     curr_flow = min(curr_flow, G[parent][i][1])
#                     break
#             current = P[current]
#         max_flow += curr_flow
#         v = t
#         while v != s:
#             u = P[v]
#             for i in range(len(G[u])):
#                 if G[u][i][0] == v:
#                     G[u][i][1] -= curr_flow
#                     break
#             for i in range(len(G[v])):
#                 if G[v][i][0] == u:
#                     G[v][i][1] += curr_flow
#                     break
#             v = P[v]
#     return max_flow

def adjacency_list(V, L):
    adj_graph = [[] for _ in range(V)]
    for (x,y,c) in L:
        adj_graph[int(x-1)].append(int(y-1))
        adj_graph[int(y-1)].append(int(x-1))
    return adj_graph


def dfs_visit(G, GP, Visited, P, i):
    Visited[i] = True
    for nb in G[i]: # jakby poprawić dfs to powinno działać 100 razy szybciej
        idd = str(i) + "_" + str(nb)
        if not Visited[nb] and GP[idd] != 0:
            P[nb] = i
            dfs_visit(G, GP, Visited, P, nb)


def dfs(G, GP, s, t, P, V):
    Visited = [False for _ in range(V)]
    dfs_visit(G, GP, Visited, P, s)
    return Visited[t]


def dict(V, L):
    GP = {}
    for (x,y,c) in L:
        idd = str(int(x-1)) + "_" + str(int(y-1))
        iddBack = str(int(y-1)) + "_" + str(int(x-1))
        GP[idd] = c
        GP[iddBack] = 0
    return GP


def Ford_Fulk(G, GP, s, t, V):
    P = [None for _ in range(V)]
    max_flow = 0
    while dfs(G, GP, s, t, P, V):
        curr_flow = 10**9
        current = t
        while current != s:
            curr_flow = min(curr_flow, GP[str(P[current]) + "_" + str(current)])
            current = P[current]
        max_flow += curr_flow
        v = t
        while v != s:
            u = P[v]
            GP[str(u) + "_" + str(v)] -= curr_flow
            GP[str(v) + "_" + str(u)] += curr_flow
            v = P[v]
    return max_flow


def solution(V, L):
    G = adjacency_list(V, L)
    GP = dict(V, L)
    return Ford_Fulk(G, GP, 0, V-1, V)


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
    if True:
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
