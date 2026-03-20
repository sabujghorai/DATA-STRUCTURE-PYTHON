class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []
        

    def addEdges(self,source,destination):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)
    
    def printgraph(self):
        for vertex in self.adjacencyList:
            print(vertex, " --> " ,self.adjacencyList[vertex],end="\n")
            
