from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
grid = []
cache = [[False]*N for _ in range(N)]

def solve():
    setGrid()
    basic = getRegions()

    setColorBlindGrid()
    colorBlind = getRegions()

    print(basic, colorBlind)

def setGrid():
    for _ in range(N):
        row = list(input().strip())
        grid.append(row)

def setColorBlindGrid():
    for i in range(N):
        for j in range(N):
            cache[i][j] = False
            if grid[i][j] != 'R': continue
            grid[i][j] = 'G'

def getRegions():
    result = 0

    for i in range(N):
        for j in range(N):
            if cache[i][j]: continue
            result += 1
            bfs(i,j)

    return result

def bfs(a,b):
    q = deque([(a,b)])
    cache[a][b] = True
    COLOR = grid[a][b]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        size = len(q)

        for _ in range(size):
            x,y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if cache[nx][ny]: continue
                    if grid[nx][ny] != COLOR: continue
                    cache[nx][ny] = True
                    q.append((nx,ny))

solve()

"""
적록색약 (골드 5)

# 문제
1. 구역 수 (정상)
2. 구역 수 (적록색약)

# 입력
N (1<=N<=100)


빨강-초록 그리디 접근 불가능.
1. 서로 인접 - 같은 구역
2. 비인접 - 같은 색이긴 하나 다른 구역


단지 번호 찾기 bfs 진행

1. 정상 BFS 진행
2. R-G 통일
3. 적록색약 BFS 진행


# BFS
- 완탐 후, 방문하지 않은 좌표부터 bfs
- 방문 그래프에 방문 여부 표기
- R일 시 모두 G로 변환
"""