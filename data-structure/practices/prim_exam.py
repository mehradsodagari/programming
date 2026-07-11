import heapq 
def prim(graph,start):
    n=len(graph) 
    visited=[False]*n 
    mst_edges=[] 
    total=0 
    heap=[(0,-1,start)]
    while heap:
        weight,u,v=heapq.heappop(heap)
        if visited[v]:
            continue 
        visited[v]=True 
        if u!=-1:
            mst_edges.append((u,v,weight))
            total+=weight
        for neighbor,w in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(heap,(w,v,neighbor))
    return mst_edges,total
