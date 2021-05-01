import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def main():
    def dfs(cv, pv):
        if cache[cv] == 1: return cv
        cache[cv] = 1

        for nv in grid[cv]:
            if nv == pv: continue
            if (result := dfs(nv, cv)) >= 0:
                cache[cv] = 2
                return result if cv != result else -1
        
        return -1

    def bfs():
        q = []
        for i in range(n):
            if cache[i] == 2: q.append(i)
            else: dist[i] = -1

        while q:
            tmp = []

            for cv in q:
                for nv in grid[cv]:
                    if dist[nv] != -1: continue
                    dist[nv] = dist[cv] + 1
                    tmp.append(nv)
            
            q = tmp


    n = int(input())
    cache = [0]*n
    dist = [0]*n
    grid = [[] for _ in range(n)]

    for _ in range(n):
        a,b = map(int, input().split())
        grid[a-1].append(b-1)
        grid[b-1].append(a-1)

    dfs(0,-1)
    bfs()
    print(*dist)

if __name__ == "__main__":
    sys.exit(main())