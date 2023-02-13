from data import runtests


def check_connectivity(deleted_nodes, original_graph):
    visited = set()
    stack = [deleted_nodes[0]]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in deleted_nodes:
                if neighbor in original_graph[node] and neighbor not in visited:
                    stack.append(neighbor)
    return len(visited) == len(deleted_nodes)


def my_solve(N, channels):
    graph = {i: set() for i in range(1, N + 1)}
    original_graph = {i: set() for i in range(1, N + 1)}
    for a, b in channels:
        graph[a].add(b)
        graph[b].add(a)
        original_graph[a].add(b)
        original_graph[b].add(a)

    deleted_nodes = []

    sorted_graph = sorted(graph.items(), key=lambda x: len(x[1]), reverse=True)
    i = 0
    if not channels: return 1

    while len(sorted_graph[0][1]) > 0:
        node_to_delete = sorted_graph[0][0]
        deleted_nodes.append(node_to_delete)
        del graph[node_to_delete]
        for node, neighbors in graph.items():
            if node_to_delete in neighbors:
                neighbors.remove(node_to_delete)
        sorted_graph = sorted(graph.items(), key=lambda x: len(x[1]), reverse=True)
        i += 1

    if check_connectivity(deleted_nodes, original_graph):
        return i
    else:
        return None


runtests(my_solve)
