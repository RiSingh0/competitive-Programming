import math as mt

class Graph:
    def __init__(self,V):
        self.graph=[[] for i in range(V)]
        self.visited=[False for i in range(V)]
        self.FlatTree=[]
        self.depth=[-1 for i in range(V)]
        self.parent=[[-1 for i in range(int(mt.log2(V))+1)] for i in range(V)]
        self.FlatStart=[-1 for i in range(V)]
        self.FlatEnd=[-1 for i in range(V)]
        
    def addEdges(self):
        for _ in range(len(self.graph)-1):
            u,v=map(int, input().split())
            self.graph[u-1].append(v-1)
            self.graph[v-1].append(u-1)
            
    def FlatterDFS(self,visit,d):
        self.depth[visit]=d
        self.FlatTree.append(visit)
        self.FlatStart[visit]=len(self.FlatTree)-1
        self.visited[visit]=True
        for i in self.graph[visit]:
            if not self.visited[i]:
                self.FlatterDFS(i,d+1)
        self.FlatTree.append(visit)
        self.FlatEnd[visit]=len(self.FlatTree)-1
        
    def parentDFS(self,current,parent):
        self.parent[current][0]=parent
        for i in self.graph[current]:
            if i != parent:
                self.parentDFS(i,current)

    def setparent(self):
        for coloum in range(1,int(mt.log2(len(self.graph)))+1):
            for row in range(1,len(self.graph)):
                if self.parent[row][coloum-1] == -1:
                    continue
                self.parent[row][coloum]=self.parent[self.parent[row][coloum-1]][coloum-1]
                
    def LCA(self,a,b):
        if a>b:
            a,b=b,a
        diff=self.depth[b]-self.depth[a]
        while diff > 0:
            i=int(mt.log(diff))
            b=self.parent[b][i]
            diff-=(1 << i)
        if a==b:
            return a
        while a != b:
            a=self.parent[a][0]
            b=self.parent[b][0]
        return b

    def getWeight(self):
        self.weight=[int(i) for i in input().split()]
    
V=int(input())
gra=Graph(V)
gra.addEdges()
gra.FlatterDFS(0,1)
print("Flat Tree",gra.FlatTree)
print("Flat Start",gra.FlatStart)
print("Flat End",gra.FlatEnd)
print("Depth ",gra.depth)
gra.parentDFS(0,-1)
gra.setparent()
gra.getWeight()
print(gra.parent)

