from data import runtests


def is_clique(deleted_nodes, original_graph):
    for node1 in deleted_nodes:
        for node2 in deleted_nodes:
            if node1 != node2 and node2 not in original_graph[node1]:
                return False
    return True


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
    if not channels: return 1

    while len(sorted_graph[0][1]) > 0:
        node_to_delete = sorted_graph[0][0]
        deleted_nodes.append(node_to_delete)
        del graph[node_to_delete]
        for node, neighbors in graph.items():
            if node_to_delete in neighbors:
                neighbors.remove(node_to_delete)
        sorted_graph = sorted(graph.items(), key=lambda x: len(x[1]), reverse=True)

    if is_clique(deleted_nodes, original_graph):
        return len(deleted_nodes)
    else:
        return None


runtests(my_solve)
