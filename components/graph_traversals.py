import networkx as nx
from collections import deque

def bfs_traversal(adj_matrix, start_node=0):
    G = nx.from_numpy_array(adj_matrix)
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            neighbors = list(G.neighbors(node))
            queue.extend(neighbors)
    
    return visited

def dfs_traversal(adj_matrix, start_node=0):
    G = nx.from_numpy_array(adj_matrix)
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = list(G.neighbors(node))
            stack.extend(neighbors[::-1])  # Reverse for correct order
    
    return visited
