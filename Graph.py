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

    def print_graph(self):
        for row in self.matrix:
            print(' '.join(map(str,row)))

G = Graph(5)
G.add_edge(0,2)
G.add_edge(0,1)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(2,4)

G.print()