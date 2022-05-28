from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = float('inf')
V,E = map(int, input().split())
K = int(input())

dist = [INF]*(V+1)
dist[K] = 0

graph = [[] for _ in range(V+1)]

def dijkstra():
    q = []
    q.append((0,K))

    while q:
        weight, vertex = heappop(q)
        for w,v in graph[vertex]:
            w += weight
            if w < dist[v]:
                dist[v] = w
                heappush(q, (w,v))


for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

dijkstra()

for num in dist[1:]:
    print(num if num != INF else "INF", sep='\n')