# BFS

# from collections import deque
#
# graph = {
#     7: [19, 21, 14],
#     19: [1, 12, 31, 21],
#     1: [7],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [6, 23],
#     6: [],
#     23: [21]
# }
#
# visited = set()
#
#
# def bfs(key, graph, visited):
#     if key in visited:
#         return
#     graphs_to_print = deque([node])
#     visited.add(key)
#
#     while graphs_to_print:
#         print(graphs_to_print.popleft(), end=' ')
#         for v in graph[key]:
#             if v not in visited:
#                 visited.add(v)
#                 graphs_to_print.append(v)
#
#
# for node in graph:
#     bfs(node, graph, visited)

# DFS

# graph = {
#     7: [19, 21, 14],
#     19: [1, 12, 31, 21],
#     1: [7],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [6, 23],
#     6: [],
#     23: [21]
# }
# visited = set()
#
#
# def dfs(key, g, col):
#     if key in col:
#         return
#
#     col.add(key)
#
#     for child in g[key]:
#         dfs(child, graph, col)
#
#     print(key, end=' ')
#
#
# for node in graph:
#     dfs(node, graph, visited)


# Find all components in graph algorithm


# num_of_nodes = int(input())
# graph = []
# visited = [False] * num_of_nodes
#
# for _ in range(num_of_nodes):
#     graph_lines = [int(el) for el in input().split()]
#     graph.append(graph_lines)
#
#
# def dfs(node, graph, visited, curr_collection):
#     if visited[node]:
#         return
#     visited[node] = True
#
#     for child in graph[node]:
#         dfs(child, graph, visited, curr_collection)
#     curr_collection.append(node)
#
#
# for node in range(num_of_nodes):
#     if visited[node]:
#         continue
#     curr_collection = []
#     dfs(node, graph, visited, curr_collection)
#     print(f"Connected component: {' '.join(str(el) for el in curr_collection)}")


# Topological sort
# def find_dependencies(key, dictionary, g):
#     if key not in dictionary:
#         dictionary[key] = 0
#
#     for child in g[key]:
#         if child not in dictionary:
#             dictionary[child] = 0
#         dictionary[child] += 1
#
#
# def find_node_without_dependencies(dictionary):
#     for key, value in dictionary.items():
#         if value == 0:
#             return key
#     return None
#
#
# def topological_sort(graph, dictionary, sorted_graph):
#     while dictionary:
#         node = find_node_without_dependencies(dictionary)
#         if node:
#             dictionary.pop(node)
#             sorted_graph.append(node)
#             for child in graph[node]:
#                 dictionary[child] -= 1
#         else:
#
#             break
#     return sorted_graph
#
#
# nodes_count = int(input())
# graph = {}
# dependencies_dict = {}
# sorted_graph = []
#
# for _ in range(nodes_count):
#     node_inp = input().split(' ->')
#     graph[node_inp[0]] = [] if not node_inp[1] else [el for el in node_inp[1].strip().split(', ')]
#
# for node in graph:
#     find_dependencies(node, dependencies_dict, graph)
#
# result_sorting = topological_sort(graph, dependencies_dict, sorted_graph)
# invalid_result = 'Invalid topological sorting'
# valid_sorting = ', '.join(result_sorting)
#
# if result_sorting:
#     print(f'Topological sorting: {valid_sorting}')
# else:
#     print(invalid_result)
