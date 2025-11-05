from collections import deque

class Graph:

    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start,end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor,visited)

    def bfs(self,start):
        visited=set()
        queue=deque([start])
        visited.add(start)

        while queue:
            vertex=queue.popleft()
            print(vertex,end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

if __name__=="__main__":

 g=Graph()

 n=int(input("Enter number of edges:-"))
 print("Enter edges(u,v):-")

 for _ in range(n):
     u,v=input().split()
     g.add_edge(u,v)

 start=input("Enter the starting vertex:-")

 print("\n DFS:-")
 g.dfs(start)

 print("\n bFS:-")
 g.bfs(start)