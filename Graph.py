class Graph:
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for i in range(vertex)]
        self.size = vertex
    
    def add_edge(self,source,destination):
        if(self.size > source >= 0 and self.size > destination >= 0):
            self.matrix[source][destination] = 1
            self.matrix[destination][source] = 1
        else:
            print("The Edge you have entered is invalid..")
    