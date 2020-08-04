class Graph:
    def __init__(self,V):
        self.graph=[[] for i in range(V+1)]
        self.Visited=set()
        
    def addEdges(self):
        for _ in range(len(self.graph)-2):
            u,v=map(int, input().split())
            self.graph[u].append(v)
            self.graph[v].append(u)
            
    def DFS(self,Node):
        print(Node)
        self.Visited.add(Node)
        for each in self.graph[Node]:
            if each not in self.Visited:
                self.DFS(each)
    
V=int(input())
gra=Graph(V)
gra.addEdges()
gra.DFS(3)



