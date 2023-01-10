import heapq
from data import runtests


def dijkstra(adj_matrix, source, sink):
    distances = [float('inf') for _ in range(len(adj_matrix))]
    predecessors = [None for _ in range(len(adj_matrix))]

    distances[source] = 0
    min_priority_queue = [(0, source)]

    while min_priority_queue:
        curr_distance, curr_node = heapq.heappop(min_priority_queue)
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[curr_node][neighbor] != 0:
                distance = curr_distance + adj_matrix[curr_node][neighbor]
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


def update_graph(adj_matrix, path, current_base_salary_i, base_salaries, source):
    adj_matrix[path[1]][path[2]] = float('inf')
    to_change = path[1]
    current_base_salary_i[to_change] += 1
    index = current_base_salary_i[to_change]
    if index < len(base_salaries[to_change - 1]):
        adj_matrix[source][to_change] = base_salaries[to_change - 1][index] - adj_matrix[source][to_change]
    else:
        adj_matrix[source][to_change] = float('inf')



def my_solve(N, M, K, base_salaries, bonuses, equipment_prices):

    # Create an adjacency matrix to represent the graph
    adj_matrix = [[0 for _ in range(N + M + 2)] for _ in range(N + M + 2)]

    source = 0
    sink = N + M + 1

    # Add edges from the source to the magicians
    for i in range(N):
        adj_matrix[source][i + 1] = base_salaries[i][0]
    current_base_salary_i = [0 for _ in range(N + 1)]

    # Add edges from the magicians to the shows
    for i in range(N):
        for j, bonus in bonuses[i]:
            adj_matrix[i + 1][N + j] = bonus

    # Add edges from the shows to the sink
    for i in range(M):
        adj_matrix[N + i + 1][sink] = equipment_prices[i]

    # Do Dijkstra's algorithm for K times updating graph
    result = 0
    for _ in range(K):
        path, cost = dijkstra(adj_matrix, source, sink)
        update_graph(adj_matrix, path, current_base_salary_i, base_salaries, source)
        result += cost
    return result


runtests(my_solve)


# print(my_solve(3, 4, 5, [(3, 8), (1, 4, 11), (5, 13)], [
#      [(1, 15), (2, 7)], # first artist shows
#      [(2, 11), (3, 17)], # second artist shows
#      [(1, 25), (2, 17), (4, 31)] # third artist shows
#    ], [5, 3, 10, 7]))
