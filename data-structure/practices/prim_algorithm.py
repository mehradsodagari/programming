from min_heap import MinHeap
class Prim:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[]for _ in range(vertices)]
    def add_edge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))    
    def mst(self,start=0):
        visited=[False]*self.vertices
        mst_edges=[]
        total_weight=0
        heap=MinHeap()
        heap.insert((0,start,-1))         
        while not heap.is_empty() and len(mst_edges)<self.vertices-1:
            weight,u,parent=heap.extract_min()            
            if visited[u]:
                continue            
            visited[u]=True            
            if parent!=-1:
                mst_edges.append((parent,u,weight))
                total_weight+=weight
           
            for v,w in self.graph[u]:
                if not visited[v]:
                    heap.insert((w,v,u))        
        return mst_edges,total_weight