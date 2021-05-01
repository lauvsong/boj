# 단지번호붙이기
import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

n = int(input())
m = [list(map(int, list(input()))) for _ in range(n)]
homes = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    m[x][y]=0
    cnt=1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if m[nx][ny]:
                    m[nx][ny]=0
                    q.append((nx,ny))
                    cnt+=1

    return cnt



for i in range(n):
    for j in range(n):
        if m[i][j]:
            homes.append(bfs(i,j))

homes.sort()
print(len(homes))
print('\n'.join(map(str, homes)))