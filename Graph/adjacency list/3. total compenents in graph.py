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
    
    def dfs(self, vertex):
        visited = set()
        stack = deque()

        visited.add(vertex)
        stack.append(vertex)

        while stack:
            curr_vertex = stack.pop()
            print(curr_vertex)

            for neighbour in self.graph[curr_vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)

    def dfs_recursive(self, vertex, visited):
        if visited is None:
            visited = set()

        visited.add(vertex)
        print(vertex)

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.dfs_recursive(neighbour, visited)
    
    def count_component_bfs(self):
        visited = set()
        count_component = 0

        for vertex in self.graph:
            if vertex not in visited:
                count_component += 1
                queue = deque()

                visited.add(vertex)
                queue.append(vertex)

                while queue:
                    curr_vertex = queue.popleft()

                    for neighbour in self.graph[curr_vertex]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
        
        return count_component
    
    def count_component_dfs(self):
        visited = set()
        count_component = 0

        for vertex in self.graph:
            if vertex not in visited:
                count_component += 1

                stack = deque()
                stack.append(vertex)
                visited.add(vertex)

                while stack:
                    curr_vertex = stack.pop()

                    for neighbour in self.graph[curr_vertex]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            stack.append(neighbour)

        return count_component 

    
if __name__ == "__main__":
    g = Graph()

    # Component 1
    g.add_edges(1, 2)
    g.add_edges(2, 3)

    # Component 2
    g.add_edges(4, 5)

    # Component 3 (cycle)
    g.add_edges(6, 7)
    g.add_edges(7, 8)
    g.add_edges(8, 6)

    # Component 4 (isolated node)
    g.add_vertex(9)

    """
    1 — 2 — 3

    4 — 5

    6 — 7
    \   /
    8

    9
    """
    print(g.count_component_bfs())
    print(g.count_component_dfs())

