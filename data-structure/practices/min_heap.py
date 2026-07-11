class MinHeap:
    def __init__(self):
        self.heap=[] 
    def parent(self,index):
        if not 0<index<len(self.heap):
            return None 
        parent=(index-1)//2
        return self.heap[parent] 
    def left_child(self,index):
        if not 0<=index<len(self.heap):
            return None 
        left=2*index+1 
        if left<len(self.heap):
            return self.heap[left] 
        return None 
    def right_child(self,index):
        if not 0<=index<len(self.heap):
            return None 
        right=2*index+2 
        if right<len(self.heap):
            return self.heap[right] 
        return None 
    def insert(self,value):
        self.heap.append(value)
        i=len(self.heap)-1 
        while i>0:
            parent=(i-1)//2 
            if self.heap[i]<self.heap[parent]:
                self.swap(i,parent)
                i=parent 
            else:
                break 
        return self.heap 
    def delete(self,value):
        if not self.heap or value not in self.heap or value is None:
            return None 
        index=self.heap.index(value) 
        removed_item=self.heap[index] 
        last_element=self.heap.pop() 
        if index<len(self.heap):
            self.heap[index]=last_element 
            if index>0 and self.heap[index]<self.heap[(index-1)//2]:
                self.reconstruct_up(index) 
            else:
                self.reconstruct_down(index,len(self.heap))
        return removed_item
    def size(self):
        return len(self.heap) 
    def get_min(self):
        return self.heap[0] if self.heap else None 
    def is_empty(self):
        return len(self.heap)==0 
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def extract_min(self):
        if not self.heap:
            return None 
        if len(self.heap)==1:
            return self.heap.pop() 
        min_value=self.heap[0]
        self.heap[0]=self.heap.pop() 
        self.reconstruct_down(0,len(self.heap))
        return min_value 
    def reconstruct_up(self,i):
        while i>0 and self.heap[i]<self.heap[(i-1)//2]:
            loc=(i-1)//2
            self.swap(i,loc)
            i=loc 
    def reconstruct_down(self,i,n):
        while True:
            smallest=i 
            left=2*i+1 
            right=2*i+2 
            if left<n and self.heap[left]<self.heap[smallest]:
                smallest=left 
            if right<n and self.heap[right]<self.heap[smallest]:
                smallest=right 
            if smallest!=i:
                self.swap(i,smallest)
                i=smallest 
            else:
                break 
