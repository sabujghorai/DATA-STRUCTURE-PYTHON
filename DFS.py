class Graph :
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for i in range(vertex)]
        self.size = vertex

    def add_edge(self,source,destination):
        if(0<=source<self.size and 0<=destination<self.size):
            self.matrix[source][destination] = 1
            self.matrix[destination][source] = 1
        else:
            print("Invalid Edge..")

    def DFS(self,source):
        visited = [False]*self.size
        stack = [source]

        while(len(stack) > 0):
            v = stack.pop()
            if(visited[v]==False):
                print(v,end = " -> ")
                visited[v] =True
                
            for i in range(self.size):
                if self.matrix[v][i] == 1 and visited[i] == False :
                    stack.append(i)

G = Graph(6)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,5)
G.add_edge(4,5)

G.DFS(0)
