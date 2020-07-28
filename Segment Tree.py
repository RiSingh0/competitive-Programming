from math import ceil,log
def binpow(a,b):
    res=1
    while b > 0 :
        #print(res,a,b)
        if b & 1 :res = res * a
        a *= a
        b >>= 1
    return res

class STree:
    def __init__(self,arr):
        #size
        self.arr_size = len(arr)-1
        
        #Till depth
        height=ceil(log(self.arr_size+1,2))
        #N*N -1
        ST_size = ( 2 * binpow(2,height) ) - 1
        #Initialize by None
        self.ST=[None for _ in range(ST_size)]
        #Build Tree
        self.build_ST(arr, 0, 0, self.arr_size)

    
    def build_ST(self,arr,ind,L,R):
        #when can't divide
        if L == R:
            self.ST[ind] = arr[L]
            return self.ST[ind]
        #Get mid
        mid = L + (R - L)//2
        #Get sum from both side
        self.ST[ind]=self.build_ST(arr, ind*2+1, L, mid)+self.build_ST(arr, ind*2+2, mid+1, R)
        #return current
        return self.ST[ind]

    def search_Query(self,L,R):
        #is_Valid
        if L > R or L < 0 or R > self.arr_size:
            return None
        #take Help
        return self.search_Help( 0, 0, self.arr_size, L, R)
    
    def search_Help(self, ind, start, end, L, R):
        #Totally Inside
        if L <= start and R >= end:
            return self.ST[ind]
        #Totally Outside
        if end < L or start > R:
            return 0
        #take mid
        mid=(start+(end-start)//2)
        
        #go both side
        return self.search_Help(2*ind+1,start,mid,L,R)+self.search_Help(2*ind+2,mid+1,end,L,R)
    
    def update_Query(self, arr, ind, val):
        #False input
        if ind < 0 or ind > self.arr_size:
            return None
        #difference to update
        diff=val-arr[ind]
        #update in array
        arr[ind]=val
        #take Help
        self.help_Update( 0, self.arr_size, ind, diff,0)
    
    def help_Update(self, start, end, update_ind, diff, curr_ind):
        
        #if not in range back
        if update_ind < start or update_ind > end:
            return
        
        #if in range update and check others
        self.ST[curr_ind] += diff

        #To stop recursion
        if start != end:
            mid = start + (end-start)//2
            self.help_Update(start, mid, update_ind, diff, curr_ind*2 +1)
            self.help_Update(mid+1, end, update_ind, diff, curr_ind*2 +2)
            
arr = [10, 11, 45, 89, 95]
print(arr)
st=STree(arr)
print(st.ST)
print(st.search_Query(2,4))
st.update_Query(arr,3,5)
print(st.search_Query(2,4))
