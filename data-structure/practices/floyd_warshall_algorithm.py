class FloydWarshall:
    def __init__(self,n):
        self.n=n
        self.INF=float('inf')
        self.dist=[[self.INF]*n for _ in range(n)]
        self.next=[[-1]*n for _ in range(n)]
        for i in range(n):
            self.dist[i][i]=0
            self.next[i][i]=i
    def add_edge(self,u,v,w):
        if w<self.dist[u][v]:
            self.dist[u][v]=w
            self.next[u][v]=v
    def add_undirected_edge(self,u,v,w):
        self.add_edge(u,v,w)
        self.add_edge(v,u,w)
    def run(self):
        for k in range(self.n):
            for i in range(self.n):
                if self.dist[i][k]==self.INF:
                    continue
                for j in range(self.n):
                    if self.dist[k][j]==self.INF:
                        continue
                    if self.dist[i][k]+self.dist[k][j]<self.dist[i][j]:
                        self.dist[i][j]=self.dist[i][k]+self.dist[k][j]
                        self.next[i][j]=self.next[i][k]
        for i in range(self.n):
            if self.dist[i][i]<0:
                return False
        return True
    def get_distance(self,u,v):
        return self.dist[u][v]
    def get_path(self,u,v):
        if self.next[u][v]==-1:
            return[]
        path=[u]
        while u!=v:
            u=self.next[u][v]
            path.append(u)
        return path