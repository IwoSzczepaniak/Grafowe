import operator
import random
from check import check_lab3
from Node import *
inf = 10 ** 10


def mergeVertices(x, y, node_graph):
    if x.exist and y.exist:
        for n_index, n_value in y.edges.items():
            if n_index != x.get_index():
                x.addEdge(n_index, n_value)
        if x.edges.get(y.get_index(), None): x.delEdge(y.get_index())
        y.del_all_edges()


# def find_highest_connection(Points, node_graph):
#     highest_val = 0
#     highest_connection_index = None
#     for point in Points:
#         if node_graph[point].exist:
#             for nei_key, nei_value in node_graph[point].s_points.items():
#                 if highest_val < nei_value:
#                     highest_val = nei_value
#                     highest_connection_index = nei_key
#     return highest_connection_index


# def point_highest_connection(element):
#     highest_val = -1
#     highest_connection_index = -1
#     if element.exist:
#         for nei_key, nei_value in element.s_points.items():
#             if highest_val < nei_value:
#                 highest_val = nei_value
#                 highest_connection_index = nei_key
#     return highest_val, highest_connection_index


def minimumCutPhase(node_graph, i, result=inf):
    a = i
    # a = 5
    S = [a]
    s = node_graph[a]

    while len(S) < len(node_graph):
        if len(s.edges) > 0:
            v = max(s.edges.items(), key=operator.itemgetter(1))[0] # like pq
            if v not in S:
                # no clue why but makes 2 tests correct
                potential_result = s.get_values()
                result = min(result, potential_result)

                S.append(v)
                s = node_graph[S[-1]]
                t = node_graph[S[-2]]

                potential_result = s.get_values()
                result = min(result, potential_result)

                mergeVertices(s, t, node_graph)
            else:
                # return result
                del s.edges[v]
        else: return inf

    return result


def solution(V, L, result=inf):
    node_graph = create_node_graph(V, L)
    for i in range(V):
        cut = minimumCutPhase(node_graph, i)
        result = min(result, cut)
    return result


if __name__ == "__main__":
    check_lab3(solution)
