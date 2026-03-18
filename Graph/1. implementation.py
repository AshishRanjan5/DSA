"""

"""
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def bfs(self, start_vertex):
        visited = set()
        queue = deque()

        visited.add(start_vertex)
        queue.append(start_vertex)

        while queue:
            curr_vertex = queue.popleft()
            print(curr_vertex)
        
            for neighbour in self.graph[curr_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
    

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.bfs('A')
