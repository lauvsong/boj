from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([1])
    cache = [False]*(n+1)
    ans = -1

    while q:
        node = q.popleft()
        if not cache[node]:
            cache[node] = True
            q += grid[node]
            ans += 1
    
    return ans


n = int(input())
m = int(input())
grid = [[] for _ in range(n+1)]

for _ in range(m):
    i,j = map(int, input().split())
    grid[i].append(j)
    grid[j].append(i)

print(bfs())