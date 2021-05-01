# DFS와 BFS
import sys
from collections import deque

def dfs():
    dfs = []
    stack = [v]
    visit = [0]*(n+1)

    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node]=1
            dfs.append(node)
            stack += graph[node] 

    return dfs

def bfs():
    for g in graph:
        g.sort()
        
    bfs=[]
    q = deque()
    q.append(v)

    visit = [0]*(n+1)

    while q:
        node = q.popleft()
        if not visit[node]:
            visit[node]=1
            bfs.append(node)
            q += graph[node]

    return bfs



n ,m ,v = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    num1, num2 = map(int, sys.stdin.readline().strip().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for g in graph:
    g.sort(reverse=True)

print(" ".join(map(str, dfs())))
print(" ".join(map(str, bfs())))