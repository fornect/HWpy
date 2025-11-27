class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.visited = list()
        self.complete = False
        self.index = 0

    def dfs(self) -> list[int]:
        states = {"white": [v for v in self.vertices], "gray": list(), "black": list()}

        def dfs_step(vertex):
            self.visited.append(vertex)
            states["gray"].append(vertex)
            states["white"].remove(vertex)
            for edge in self.edges:
                if edge[0] == vertex:
                    if edge[1] in states["white"]:
                        dfs_step(edge[1])
                if edge[1] == vertex:
                    if edge[0] in states["white"]:
                        dfs_step(edge[0])
            states["black"].append(vertex)
            states["gray"].remove(vertex)

        for vertex in self.vertices:
            if vertex in states["white"]:
                dfs_step(vertex)
        self.complete = True
        return self.visited
    
    def __iter__(self):
        if not self.complete:
            self.visited = self.dfs()
            self.complete = True
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.visited):
            raise StopIteration
        vertex = self.visited[self.index]
        self.index += 1
        return vertex