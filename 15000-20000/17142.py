from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

EMPTY = '0'
WALL = '1'
INACTIVE = '2'

def bfs(comb):
    dist = copy.deepcopy(grid)
    time = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for x,y in comb:
        dist[x][y] = 0

    q = deque(comb)
    cnt = 0

    while q:
        if empty_cnt == cnt:
            break

        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n  and 0 <= ny < n:

                if dist[nx][ny] == WALL:
                    continue

                if dist[nx][ny] == INACTIVE:
                    dist[nx][ny] = dist[x][y] + 1
                    time = dist[nx][ny]
                    q.append((nx,ny))
                
                elif dist[nx][ny] == EMPTY:
                    cnt += 1
                    dist[nx][ny] = dist[x][y] + 1
                    time = dist[nx][ny]
                    q.append((nx,ny))

        if ans <= time:
            return sys.maxsize

    for row in dist:
        if EMPTY in row:
            time = -1
            break

    return time
            

n,m = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(n)]
viruses = []
empty_cnt = 0

ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if grid[i][j] == INACTIVE:
            viruses.append((i,j))
        elif grid[i][j] == EMPTY:
            empty_cnt += 1

for comb in combinations(viruses, m):
    res = bfs(comb)
    if res == -1: continue
    ans = min(ans, res)

if ans == sys.maxsize:
    ans = -1

print(ans)

"""
# 문제
모든 빈칸에 바이러스가 있게 되는 최소 시간 (불가능한 경우 -1)

# 변수
n (4 <= n <= 50)
m (1 <= m <= 10)


# 알고리즘

1. 바이러스 조합 DFS
- 최소 시간 갱신

전체 바이러스 개수 ^ 놓을 수 있는 바이러스 개수 = 10 ^ 10 = 10000000000
10! * 10 = 36288000

조합 가능.


2. 조합 별로 BFS

"""

