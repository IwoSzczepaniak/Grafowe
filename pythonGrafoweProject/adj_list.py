from data import runtests
import heapq
from collections import defaultdict


def dijkstra(graph, source, sink):
    distances = [float('inf') for _ in range(len(graph)+1)]
    predecessors = [None for _ in range(len(graph)+2)]
    distances[source] = 0
    min_priority_queue = [(0, source)]
    while min_priority_queue:
        curr_distance, curr_node = heapq.heappop(min_priority_queue)
        for neighbor, weight in graph[curr_node]:
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = curr_node
                heapq.heappush(min_priority_queue, (distance, neighbor))

    shortest_path = []
    curr_node = sink
    while curr_node is not None:
        shortest_path.append(curr_node)
        curr_node = predecessors[curr_node]
    shortest_path = shortest_path[::-1]
    return shortest_path, distances[sink]


def update_graph(graph, path, current_base_salary_i, base_salaries, source):
    for element in graph[path[1]]:
        if element[0] == path[2]:
            graph[path[1]].remove(element)
            break
    to_change = path[1]
    current_base_salary_i[to_change] += 1
    index = current_base_salary_i[to_change]
    if index < len(base_salaries[to_change - 1]):
        for element in graph[source]:
            if element[0] == to_change:
                graph[source].remove(element)
                break
        graph[source].append((to_change, base_salaries[to_change - 1][index] - base_salaries[to_change - 1][index-1]))
    else:
        for element in graph[source]:
            if element[0] == to_change:
                graph[source].remove(element)
                break


def my_solve(N, M, K, base_salaries, bonuses, equipment_prices):
    graph = defaultdict(list)
    source = 0
    sink = N + M + 1

    for i in range(N):
        graph[source].append((i + 1, base_salaries[i][0]))
    current_base_salary_i = [0 for _ in range(N + 1)]

    for i in range(N):
        for j, bonus in bonuses[i]:
            graph[i + 1].append((N + j, bonus))

    # Add edges from the shows to the sink
    for i in range(M):
        graph[N + i + 1].append((sink, equipment_prices[i]))

    # Do Dijkstra's algorithm for K times updating graph
    result = 0
    for _ in range(K):
        path, cost = dijkstra(graph, source, sink)
        update_graph(graph, path, current_base_salary_i, base_salaries, source)
        result += cost
    return result

runtests(my_solve)