class Kruskal:
    def __init__(self,size):
        self.size=size 
        self.parent=list(range(size))
        self.rank=[0]*size 
    def find(self,index):
        if self.parent[index]!=index:
            self.parent[index]=self.find(self.parent[index]) 
        return self.parent[index] 
    def union(self,x,y):
        rx,ry=self.find(x),self.find(y) 
        if rx==ry:
            return False 
        if self.rank[rx]>self.rank[ry]:
            self.parent[ry]=rx 
        elif self.rank[rx]<self.rank[ry]:
            self.parent[rx]=ry
        else:
            self.parent[ry]=rx 
            self.rank[rx]+=1 
        return True 
    def mst(self,edges):
        edges.sort()
        mst_edges,total=[],0 
        for w,u,v in edges:
            if self.union(u,v):
                mst_edges.append((u,v,w)) 
                total+=w 
                if len(mst_edges)==self.size-1:
                    break 
        return mst_edges,total 
