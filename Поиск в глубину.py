from typing import Dict, List

class Graph:
    def __init__(self):
        self.adjacency_list: Dict[int, List[int]] = {}

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)


def dfs(graph: Dict[int, List[int]], start_vertex: int) -> List[int]:
    visited = []
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in graph:  
                stack.extend(set(graph[vertex]) - set(visited))

    return visited


def find_connected_component(graph: Graph) -> List[int]:
    if not graph.adjacency_list:
        return []

    first_vertex = next(iter(graph.adjacency_list))

    return dfs(graph.adjacency_list, first_vertex)


n, m = map(int, input().split())
graph = Graph()
for i in range(n):
    graph.add_vertex(i + 1)
for i in range(m):
    x, y = map(int, input().split())
    graph.add_edge(x, y)

connected_component = find_connected_component(graph)
print(len(connected_component))
connected_component.sort()
for i in connected_component:
    print(i, end = " ")
