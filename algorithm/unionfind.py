class UnionFind:
    def __init__(self, num):
        self.par = [i for i in range(num+1)]
        self.rank = [0] * (num+1)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if self.rank[ru] < self.rank[rv]:
            self.par[ru] = rv
        else:
            self.par[rv] = ru
            if self.rank[ru] == self.rank[rv]:
                self.rank[ru] += 1

    def same(self, u, v):
        return self.root(u) == self.root(v)


# AtCoder example, ABC075C
if __name__ == '__main__':
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    ans = 0

    for i in range(M):
        uni = UnionFind(N)
        for j in range(M):
            if i != j:
                uni.unite(data[j][0], data[j][1])
            else:
                check = j
        if not uni.same(data[check][0], data[check][1]):
            ans += 1

    print(ans)

