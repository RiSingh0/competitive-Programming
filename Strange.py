from sys import setrecursionlimit
setrecursionlimit(10**6)
from bisect import bisect_left as Lower_Bound

def create_new():
    check = dict()
    for i in range(n-1, -1, -1):
        parent[pi[i]] = pi[i]
        for j in Graph[pi[i]]:
            if j in check:
                z = find(j)
                parent[z] = pi[i]
                newGraph[pi[i]].append(z)
                newGraph[z].append(pi[i])
        check[pi[i]] = "Present"
    
def DFS(x):
    visited.add(x)
    days_Stack.append(Trackdays[x])
    
    if ai_Stack == []:
        ai_Stack.append(ai[x])
    else:
        ai_Stack.append(ai_Stack[-1]+ai[x])
        
    z = Lower_Bound(ai_Stack,bi[x])
    
    if z < len(days_Stack):
        ans[x]=days_Stack[z]
        
    for i in newGraph[x]:
        if i not in visited:
            DFS(i)
            
    days_Stack.pop(-1)
    ai_Stack.pop(-1)
    
def find(x):
    if x == parent[x]:
        return x
    z = find(parent[x])
    parent[x] = z
    return z

t=int(input())
for you in range(t):
    n=int(input())

    Graph=[[] for i in range(n)]

    for i in range(n-1):
        u,v=map(int,input().split())
        Graph[u-1].append(v-1)
        Graph[v-1].append(u-1)

    pi=[int(i)-1 for i in input().split()]
    ai=[int(i) for i in input().split()]
    bi=[int(i) for i in input().split()]
    
    newGraph=[[] for i in range(n)]
    parent=[-1 for i in range(n)]
    create_new()
    
    Trackdays=dict()
    for i in range(n):
        Trackdays[pi[i]] = i + 1
        
    ans=[-1 for i in range(n)]
    visited=set()
    days_Stack=list()
    ai_Stack=list()
    
    DFS(pi[0])
    
    print(*ans)
    
