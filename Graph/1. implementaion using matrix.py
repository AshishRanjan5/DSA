from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.matrix = []
        self.size = 0
        self.directed = directed
    
    def add_node(self):
        for row in self.matrix:
            row.append(0)

        self.size += 1
        self.matrix.append([0]* self.size)
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 < 0 or vertex2 < 0:
            raise IndexError("Index out of bound")

        while self.size <= max(vertex1, vertex2):
            self.add_node()

        if not self.directed:
            self.matrix[vertex1][vertex2] = 1
            self.matrix[vertex2][vertex1] = 1
        else:
            self.matrix[vertex1][vertex2] = 1
    
    def build_graph_dynamically(self, edges):
        for vertex1, vertex2 in edges:
            self.add_edge(vertex1, vertex2)
        
    def build_graph_optimally(self, edges):
        N = max(max(u,v) for u,v in edges) + 1

        self.matrix = [[0 for _ in range(N)] for _ in range(N)]
        self.size = N

        for u, v in edges:
            if not self.directed:
                self.matrix[u][v] = 1
                self.matrix[v][u] = 1
            else:
                self.matrix[u][v] = 1
    
    def bfs(self, vertex):
        visited = set()
        queue = deque()

        visited.add(vertex)
        queue.append(vertex)

        while queue:
            curr_vertex = queue.popleft()
            print(curr_vertex)
            for neighbour in range(self.size):
                if self.matrix[curr_vertex][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


    def dfs(self, vertex):
        visited = set()
        stack = deque()

        visited.add(vertex)
        stack.append(vertex)

        while stack:
            curr_vertex = stack.pop()
            print(curr_vertex)

            for neighbour in range(self.size):
                if self.matrix[curr_vertex][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
    
    def dfs_recursively(self, vertex, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(vertex)
        print(vertex)

        for neighbour in range(self.size):
            if self.matrix[vertex][neighbour] == 1 and neighbour not in visited:
                    self.dfs_recursively(neighbour, visited)


if __name__ == "__main__":
    g = Graph()

    edges = [[0,1], [1,2]]

    g.build_graph_optimally(edges)

    g.bfs(1)
    g.dfs(1)
