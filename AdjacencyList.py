class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []
