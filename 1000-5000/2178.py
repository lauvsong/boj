# 미로 탐색
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dist=[[0]*m for _ in range(n)]

    q = deque()
    q.append((x,y))
    dist[x][y]=1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n : continue
            if ny < 0 or ny >= m : continue 
            if graph[x][y] == 0 : continue
            if dist[nx][ny] != 0: continue

            q.append((nx,ny))
            dist[nx][ny]=dist[x][y]+1


    return dist[n-1][m-1]


n,m  = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

print(bfs(0,0))
