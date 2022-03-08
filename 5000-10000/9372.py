from collections import deque
import sys
input = sys.stdin.readline

UNCACHED = -2

cache = []
graph = []

v = 0
e = 0

def bfs(start):
    q = deque([start])
    cache[start] = 1

    while q:
        node = q.popleft()
        
        for child in graph[node]:
            if cache[child] == UNCACHED:
                cache[child] = -cache[node]
                q.append(child)
            else:
                if cache[child] == cache[node]:
                    return False

    return True


def run():
    global graph, cache
    v,e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    cache = [UNCACHED] * (v + 1)

    ans = "YES"

    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for node in range(1,v+1):
        if cache[node] == UNCACHED:
            res = bfs(node)
            if not res:
                ans = "NO"
                break
    
    return ans

k = int(input())
for _ in range(k):
    print(run())


"""
상근이의 여행

# 문제
모든 노드를 탐색하기 위해 지나야 하는 간선의 최소 개수


bfs.

탐색 중에
부모와 color가 같은 자식일 때? => 불가능.


"""
