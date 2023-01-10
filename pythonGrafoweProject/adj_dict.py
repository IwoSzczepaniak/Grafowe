# Iwo Szczepaniak
# Tworzymy graf ze źródłem oraz z ujściem, gdzie pozostałymi wierzchołkami są czarodzieje i występy.
# Gdy czarodziej może mieć dany występ dodajemy krawędź między nim a występem o wadze równej wynagrodzeniu za ten występ
# Wagą krawędzi między źródłem a czarodziejami są ceny wynagordzeń, aktualizowane za każdym wykonaniem Dijkstry
# Wagą krawędzi między występami a ujściem jest koszt ekwipunku za dany występ.

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


def update_graph(graph, path, current_base_salary_i, base_salaries, source):
    # usunięcie krawędzi między czarodziejem a występem
    del graph[path[1]][path[2]]

    # aktualizacja krawędzi między źródłem i czarodziejem
    to_change = path[1]
    current_base_salary_i[to_change] += 1
    index = current_base_salary_i[to_change]
    if index < len(base_salaries[to_change - 1]):
        graph[source][to_change] = base_salaries[to_change - 1][index] - base_salaries[to_change - 1][index - 1]
    else:
        del graph[source][to_change]


def my_solve(N, M, K, base_salaries, bonuses, equipment_prices):
    # Tworzymy graf w którym wierchołkami są czarodzieje oraz występy, a także dodajemy źródło-source oraz ujście-sink
    graph = [{} for _ in range(N + M + 2)]
    source = 0
    sink = N + M + 1

    # Dodajemy krawędzie między źródłem{0} a czarodziejami[1,N]
    for i in range(N):
        graph[source][i + 1] = base_salaries[i][0]

    # current_base_salary_i to tablica przechowująca indeksy z aktualnie należną zapłatą dla danego Maga -
    # indeks zero dodany dla uproszczenia indeksowania
    current_base_salary_i = [0 for _ in range(N + 1)]

    # Dodajemy krawędzie między czarodziejami[1,N] a ich występami[N+1,M]
    for i in range(N):
        for j, bonus in bonuses[i]:
            graph[i + 1][N + j] = bonus

    # Dodajemy krawędzie od występów[N+1,M] do ujścia{N+M+1}
    for i in range(M):
        graph[N + i + 1][sink] = equipment_prices[i]

    # Wykonujemy Dijkstrę K razy, za każdym razem aktualizując graf
    result = 0
    for _ in range(K):
        path, cost = dijkstra(graph, source, sink)
        update_graph(graph, path, current_base_salary_i, base_salaries, source)
        result += cost

    return result


runtests(my_solve)
