class MaxHeap:
    #initilize Heap
    def __init__(self):
        self.heap=[]
        
    #Shift Up
    def pushUp(self,ind):
        try:
            #Till child is Greater
            while self.heap[ind] > self.heap[(ind - 1)//2] and (ind-1)//2 >= 0:
                
                #swap current node with parent
                self.heap[ind], self.heap[(ind - 1)//2] = self.heap[(ind - 1)//2], self.heap[ind]
                
                #now current node at parent index
                ind=(ind - 1 )//2
        except:
            pass
        
    def pushDown(self,ind):
        #initilize Right Child, Left Child
        Rchild=(ind*2)+2
        Lchild=(ind*2)+1
        
        try:
            #Till current is smaller then any of child
            while (self.heap[ind] < self.heap[Lchild]) or (self.heap[ind] < self.heap[Rchild]):
                
                #swap with Left Child
                if self.heap[Lchild] > self.heap[Rchild]:
                    self.heap[Lchild], self.heap[ind] = self.heap[ind], self.heap[Lchild]
                    ind=Lchild
                #swap with Right Child
                else:
                    self.heap[Rchild], self.heap[ind] = self.heap[ind], self.heap[Rchild]
                    ind=Rchild
                #re-initilize RightChild,LeftChild
                Rchild=(ind*2)+2
                Lchild=(ind*2)+1
        except:
            try:
                #if contain left but Exception of just Right Child
                if self.heap[ind] < self.heap[Lchild]:
                    self.heap[Lchild], self.heap[ind] = self.heap[ind], self.heap[Lchild]
            except:
                pass
            
    #Insert new value
    def insert(self,data):
        #append at last
        self.heap.append(data)
        
        #balance the heap
        self.pushUp(len(self.heap) - 1)

        
    #Remove Max value
    def remove(self):
        #if already empty
        if len(self.heap) < 1:
            return None
        
        #swap 1st with last
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        
        #take last val in popVal
        popVal=self.heap.pop()
        
        #Again balance the Heap
        self.pushDown(0)
        
        return popVal
        
    

my=MaxHeap()
my.insert(10)
my.insert(760)
my.insert(13)
my.insert(11)
my.insert(15)
my.insert(70)
my.insert(20)
my.insert(100)
my.insert(110)
print(my.heap)
print(my.remove())
print(my.remove())
print(my.remove())
print(my.remove())
print(my.remove())
print(my.remove())
print(my.remove())
print(my.remove())
print(my.remove())
