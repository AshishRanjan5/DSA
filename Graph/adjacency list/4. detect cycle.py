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
    
    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(vertex)
        print(vertex)

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)
    
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
                    queue.append(neighbour)
                    visited.add(neighbour)
    

    def dfs_iteratively(self, vertex):
        visited = set()
        stack = deque()

        visited.add(vertex)
        stack.append(vertex)

        while stack:
            curr_vertex = stack.pop()
            print(curr_vertex)

            for neighbour in self.graph[curr_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
    
    def detectCycle(self, vertex, parent=None, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(vertex)

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                if self.detectCycle(neighbour, vertex, visited):
                    return True
            
            elif neighbour != parent:
                return True

        return False

if __name__ == "__main__":
    g = Graph()


