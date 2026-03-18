class Graph:
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for i in range(vertex)]
        self.size = vertex
        