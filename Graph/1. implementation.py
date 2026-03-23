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
    
    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(vertex)
        print(vertex)
        
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)
    
    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = deque()

        visited.add(start_vertex)
        stack.append(start_vertex)

        while stack:
            curr_vertex = stack.pop()
            print(curr_vertex)
            
            for neighbour in self.graph[curr_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

    def build_graph(self, edges):
        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]
            if vertex1 not in self.graph:
                self.graph[vertex1] = []
        
            if vertex2 not in self.graph:
                self.graph[vertex2] = []
            
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

if __name__ == "__main__":
    g = Graph()
    
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'E']]
    g.build_graph(edges)

    print("BFS\n")
    g.bfs('A')

    print("DFS\n")
    g.dfs('A')

    print("DFS Iterative using Stack\n")
    g.dfs_iterative('A')
