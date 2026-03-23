from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edges(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def build_graph(self, edges): # whenever we are just given edges as list.
        
        for vertex1, vertex2 in edges:
            if vertex1 not in self.graph:
                self.graph[vertex1] = []
            if vertex2 not in self.graph:
                self.graph[vertex2] = []
            
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        


    def bfs(self, vertex):
        visited = set()
        queue = deque()

        visited.add(vertex)
        queue.append(vertex)

        while queue:
            curr_vertex = queue.popleft()
            print(curr_vertex)
            
            for neighbour in self.graph[curr_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
    
    def pathExists(self, source_vertex, destination_vertex):
        visited = set()
        queue = deque()

        visited.add(source_vertex)
        queue.append(source_vertex)

        while queue:
            curr_vertex = queue.popleft()
            if curr_vertex == destination_vertex:
                return True
            
            for neighbour in self.graph[curr_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        
        return False


if __name__ == "__main__":
    g = Graph()

    edges = [[0, 2], [1, 2], [0, 3], [4, 5]]
    g.build_graph(edges)

    print(g.pathExists(1, 5))
    print(g.pathExists(2, 3))