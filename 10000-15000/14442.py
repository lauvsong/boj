from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
grid = tuple(input().rstrip() for _ in range(n))

q = deque([(0,0,0)])
cache = [[k+1]*m for _ in range(n)]
cache[0][0] = 0
dist = 1

while q:
    for _ in range(len(q)):
        cnt,x,y = q.popleft()

        if x == n-1 and y == m-1: 
            print(dist)
            exit()

        for i,j in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = x+i, y+j

            if 0 <= nx < n and 0 <= ny < m:

                if cache[nx][ny] > cnt:
                    if grid[nx][ny] == '0':
                        cache[nx][ny] = cnt
                        q.append((cnt,nx,ny))

                    elif cnt < k:
                        cache[nx][ny] = cnt+1
                        q.append((cnt+1,nx,ny))

    dist += 1
print(-1)