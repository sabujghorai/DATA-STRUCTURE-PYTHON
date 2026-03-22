class Graph :
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for i in range(vertex)]
        self.size = vertex

    def add_edge(self,source,destination):
        if(0<=source<self.size and 0<=destination<self.size):
            self.matrix[source][destination]
            self.matrix[destination][source]