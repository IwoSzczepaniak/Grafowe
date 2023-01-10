# Iwo Szczepaniak
# Tworzymy graf ze źródłem oraz z ujściem, gdzie pozostałymi wierzchołkami są czarodzieje i występy.
# Gdy czarodziej może mieć dany występ dodajemy krawędź między nim a występem o wadze równej wynagrodzeniu za ten występ
# Wagą krawędzi między źródłem a czarodziejami są bazowe wynagrodzenia, aktualizowane za każdym wykonaniem Dijkstry
# Wagą krawędzi między występami a ujściem są koszty ekwipunku za dany występ.

# Pomysłem na algorytm jest przejście K razy Dijkstrą po grafie, równocześnie aktualizując graf.
# Szacowana złożoność: K * (E log V)
# W komentarzach używany jest zapis matematyczny zbiorów


from data import runtests
from heapq import heappush, heappop


def dijkstra(graph, source, sink):
    dist = [float('inf') for _ in range(sink + 1)]
    prev = [None for _ in range(sink + 1)]
    dist[source] = 0
    pq = []
    heappush(pq, (0, source))
    # heapq ma lepszą wydajność niż queue.PriorityQueue()
    while pq:
        distance, node = heappop(pq)
        if node == sink: break
        for neighbor, weight in graph[node].items():
            new_distance = distance + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                prev[neighbor] = node
                heappush(pq, (new_distance, neighbor))
    path = []
    node = sink
    while node is not None:
        path.append(node)
        node = prev[node]
    return path[::-1], dist[sink]


def update_graph(graph, path, current_base_index, base, source):
    # usunięcie krawędzi między czarodziejem a występem
    del graph[path[1]][path[2]]

    # aktualizacja krawędzi między źródłem i czarodziejem
    to_change = path[1]
    current_base_index[to_change] += 1
    index = current_base_index[to_change]
    if index < len(base[to_change - 1]):
        graph[source][to_change] = base[to_change - 1][index] - base[to_change - 1][index - 1]
    else:
        del graph[source][to_change]


def my_solve(N, M, K, base, wages, eq_cost):
    # Tworzymy graf w którym wierchołkami są czarodzieje oraz występy, a także dodajemy źródło i ujście
    graph = [{} for _ in range(N + M + 2)]
    source = 0
    sink = N + M + 1

    # current_base_index to tablica przechowująca indeksy z aktualnie należną zapłatą dla danego Maga
    current_base_index = [0 for _ in range(N + 1)]

    # Dodajemy krawędzie między źródłem{0} a czarodziejami[1,N]
    for i in range(N):
        graph[source][i + 1] = base[i][current_base_index[i + 1]]

    # Dodajemy krawędzie między czarodziejami[1,N] a ich występami[N+1,M]
    for i in range(N):
        for j, wage in wages[i]:
            graph[i + 1][N + j] = wage

    # Dodajemy krawędzie od występów[N+1,M] do ujścia{N+M+1}
    for i in range(M):
        graph[N + i + 1][sink] = eq_cost[i]

    # Wykonujemy Dijkstrę K razy, za każdym razem aktualizując graf
    result = 0
    for _ in range(K):
        path, cost = dijkstra(graph, source, sink)
        update_graph(graph, path, current_base_index, base, source)
        result += cost

    return result


runtests(my_solve)
