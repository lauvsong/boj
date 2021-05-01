from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    q = deque([a])
    cache = [False]*(n+1)
    ans = 0

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == b: return ans

            for i in parent[node]:
                if not cache[i]:
                    cache[i] = True
                    q.append(i)
            
        ans += 1
    
    return -1



n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
parent = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    parent[y].append(x)
    parent[x].append(y)

print(bfs(t1, t2))