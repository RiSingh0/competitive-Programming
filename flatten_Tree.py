from math import ceil,log
def binpow(a,b):
    res=1
    while b > 0 :
        if b & 1 :res = res * a
        a *= a
        b >>= 1
    return res

class STree:
    def __init__(self,arr):
        self.arr_size = len(arr)-1
        height=ceil(log(self.arr_size+1,2))
        ST_size = ( 2 * binpow(2,height) ) - 1
        self.ST=[None for _ in range(ST_size)]
        self.build_ST(arr, 0, 0, self.arr_size)

    
    def build_ST(self,arr,ind,L,R):
        if L == R:
            self.ST[ind] = arr[L]
            return self.ST[ind]
        mid = L + (R - L)//2
        self.ST[ind]=self.build_ST(arr, ind*2+1, L, mid)+self.build_ST(arr, ind*2+2, mid+1, R)
        return self.ST[ind]

    def search_Query(self,L,R):
        if L > R or L < 0 or R > self.arr_size:
            return None
        return self.search_Help( 0, 0, self.arr_size, L, R)
    
    def search_Help(self, ind, start, end, L, R):
        if L <= start and R >= end:
            return self.ST[ind]
        if end < L or start > R:
            return 0
        mid=(start+(end-start)//2)
        return self.search_Help(2*ind+1,start,mid,L,R)+self.search_Help(2*ind+2,mid+1,end,L,R)
    
    def update_Query(self, arr, ind, val):
        if ind < 0 or ind > self.arr_size:
            return None
        diff=val-arr[ind]
        arr[ind]=val
        self.help_Update( 0, self.arr_size, ind, diff,0)
    
    def help_Update(self, start, end, update_ind, diff, curr_ind):
        if update_ind < start or update_ind > end:
            return
        self.ST[curr_ind] += diff
        if start != end:
            mid = start + (end-start)//2
            self.help_Update(start, mid, update_ind, diff, curr_ind*2 +1)
            self.help_Update(mid+1, end, update_ind, diff, curr_ind*2 +2)
            
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[[] for i in range(V+1)]
        self.Visited=set()
        self.count=0
        self.intime=dict()
        self.outtime=dict()
        
    def addEdges(self):
        self.weight=[int(x) for x in input().split()]
        for _ in range(len(self.graph)-2):
            u,v=map(int, input().split())
            self.graph[u].append(v)
            self.graph[v].append(u)
            
    def DFS(self,Node):
        self.intime[Node]=self.count
        self.count+=1
        self.Visited.add(Node)
        for each in self.graph[Node]:
            if each not in self.Visited:
                self.DFS(each)
        self.outtime[Node]=self.count
        self.count+=1
    
    def constructFlatt(self):
        self.flatt=[0 for i in range(self.V*2)]
        for i in range(1,self.V+1):
            self.flatt[self.intime[i]]=self.weight[i-1]
            self.flatt[self.outtime[i]]=(self.weight[i-1]*-1)
            
V, Q = map(int,input().split())
gra = Graph(V)
gra.addEdges()
gra.DFS(1)
gra.constructFlatt()
st = STree(gra.flatt)
for _ in range(Q):
    ty, u, v = map(int, input().split())
    if ty == 1:
        u_In = gra.intime[u]
        u_Out = gra.outtime[u]
        v_In=gra.intime[v]
        v_Out=gra.outtime[v]
        if (u_In <= v_In <= u_Out) or (v_In <= u_In <= v_Out):
            if u_In <= v_In:
                print(st.search_Query(u_In, v_In))
            else:
                print(st.search_Query(v_In, u_In))
        else:
            print(-1)
    else:
        In=gra.intime[u]
        Out=gra.outtime[u]
        st.update_Query(gra.flatt, In, v)
        st.update_Query(gra.flatt, Out, v*-1)
        gra.flatt[In]=v
        gra.flatt[Out]=(v*-1)
