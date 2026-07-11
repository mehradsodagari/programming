class Graph:
    def __init__(self):
        self.graph={}
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]
    def add_edge(self,v,u):
        self.add_node(u)
        self.add_node(v) 
        if v not in self.graph[u]:
            self.graph[u].append(v) 
        if u not in self.graph[v]:
            self.graph[v].append(u) 
    def BFS(self,start):
        if start not in self.graph:
            print(f'node {start} not found in graph')
            return []
        visited={node:False for node in self.graph}
        queue=[start] 
        visited[start]=True 
        result=[]
        while queue:
            s=queue.pop(0)
            result.append(s)
            print(s,end=' ')
            for neighbor in self.graph[s]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor]=True 
        return result
    def DFS_recursive(self,node,visited,result):
       visited[node]=True
       result.append(node)
       for neighbor in self.graph[node]:
           if not visited[neighbor]:
               self.DFS_recursive(neighbor,visited,result)
    def DFS(self,start):
        if start not in self.graph:
            print(f'node {start} not found in graph')
            return []
        visited={node:False for node in self.graph}
        result=[]
        self.DFS_recursive(start,visited,result)
        return result 
    def __repr__(self):
        return str(self.graph)
    