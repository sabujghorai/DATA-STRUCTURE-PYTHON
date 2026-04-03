from collections import deque

class Graph :
    def __init__(self,vertex):
        self.matrix = [[0]*vertex for x in range(vertex)]
        self.size = vertex
    
    def add_edge(self,source,destination):
        if(0<=source<self.size and 0<=destination<self.size):
            self.matrix = [source][destination] = 1
            self.matrix = [destination][source] = 1
        else:
            print("Invalid edge")
    
    def BSF(self,source):
        visited = [False] * self.size
        queue = deque([source])
        visited[source] = True

        while(queue): # means queue is not equal to None
            v = queue.popleft
            print(v,end = " ")

        for i in range(self.size):
            if(self.matrix[v][i] == 1 and visited[1] == False):
                visited[i] =True
                queue.append(i)

G = Graph(8)
G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(1,3)
G.add_edge(3,5)
G.add_edge(3,4)
G.add_edge(5,4)
G.add_edge(4,6)
G.add_edge(6,2)
G.add_edge(6,7)
G.BSF(0)