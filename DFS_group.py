class MYGraph:
    def __init__(self,V):
        self.graph=[[] for i in range(V)]
        self.visited=[False for i in range(V)]
        self.inlink=[[] for i in range(V)]
        
    def addEdges(self,No):
        for _ in range(No):
            u,v=map(int, input().split())
            self.graph[u-1].append(v-1)
            self.graph[v-1].append(u-1)
                       
    def DFS(self,visit,no):
        self.visited[visit]=True
        self.inlink[no].append(visit)
        for i in self.graph[visit]:
            if not self.visited[i]:
                self.DFS(i,no)
t=int(input())
for _ in range(t):
    N, M = map(int, input().split())
    Arr=[int(x) for x in input().split()]
    g=MYGraph(N)
    g.addEdges(M)
    #print(g.graph)
    group=0
    
    for i in range(N):
        if not g.visited[i]:
            #print(i)
            g.DFS(i,group)
            group+=1
