class Graph :
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for i in range(vertex)]
        self.size = vertex

    def add_edge(self,source,destination):
        if(0<=source<self.size and 0<=destination<self.size):
            self.matrix[source][destination]
            self.matrix[destination][source]
        else:
            print("Invalid Edge..")

    def DFS(self,source):
        visited = [False]*self.size
        stack = [source]

        while(len(stack) > 0):
            v = stack.pop
            if(visited[v]==False):
                print(v,end = " -> ")
                visited[v] =True
                