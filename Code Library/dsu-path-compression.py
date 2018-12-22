class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.par[xr] = yr

