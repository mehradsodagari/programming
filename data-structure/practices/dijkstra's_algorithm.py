from min_heap import MinHeap
class Dijkstra:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[] for _ in range(vertices)]
    def add_edge(self,u,v,w):
        self.graph[u].append((v,w))
    def add_undirected_edge(self,u,v,w):
        self.add_edge(u,v,w)
        self.add_edge(v,u,w) 
    def shortest_path(self,start):
        distances=[float('inf')]*self.vertices 
        parents=[-1]*self.vertices 
        distances[start]=0 
        heap=MinHeap() 
        heap.insert((0,start))
        processed=[False]*self.vertices
        while not heap.is_empty():
            current_distance,u=heap.extract_min() 
            if processed[u]:
                continue 
            processed[u]=True 
            for v,weight in self.graph[u]:
                if not processed[v]:
                    new_distance=current_distance+weight 
                    if new_distance<distances[v]:
                        distances[v]=new_distance 
                        parents[v]=u 
                        heap.insert((new_distance,v))
        return distances,parents 
    def get_path(self,parent,target):
        path=[] 
        current=target
        while current!=-1:
            path.append(current) 
            current=parent[current] 
        return path[::-1]
