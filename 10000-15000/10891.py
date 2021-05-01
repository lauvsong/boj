import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cv, pv):
    global ans
    cycle = 0
    offset = 0

    for nv in graph[cv]:
        if nv == pv: continue
        if dist[nv] == 0:
            dist[nv] = dist[cv] + 1
            cycle += dfs(nv, cv)
        elif dist[nv] < dist[cv]: cycle += 1
        elif dist[nv] > dist[cv]: offset += 1
    
    if cycle > 1: 
        print("Not cactus")
        sys.exit()
    return cycle - offset


n,m = map(int, input().split())
graph = [[] for _ in range(n)]
dist = [0]*n
cnt = [0]*n
ans = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dist[0] = 1
dfs(0,-1)

print("Cactus")