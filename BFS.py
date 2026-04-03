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