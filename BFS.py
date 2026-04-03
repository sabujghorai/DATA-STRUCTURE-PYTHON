class Graph :
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for x in range(vertex)]
        self.size = vertex
    
    def add_edge(self,source,destination):
        if(0<=source<self.size and 0<=destination<self.size):
            self.matrix = [source][destination] = 1
            self.matrix = [destination][source] = 1
            