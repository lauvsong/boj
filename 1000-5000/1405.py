import sys
input = sys.stdin.readline

def dfs(depth, curr, prob):
    global ans
    if depth == n:
        ans += prob
        return
    
    x,y = curr
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx,ny) in cache: continue

        cache.append((nx,ny))
        dfs(depth+1, (nx,ny), prob * pos[i])
        cache.pop()


n, *pos = map(int, input().split())

for i in range(4):
    pos[i] /=100

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cache = [(0,0)]
ans = 0
dfs(0, (0,0), 1)

print(ans)

"""

# 문제
같은 곳 재방문하지 않을 확률


*동서남북 총합 100

0 <= 동서남북 <= 100
0 <= n <= 14



전체 경우 중
단순한 것의 비율을 구하면 됨.

1. 전체 경로 경우의 수 탐색
    - 단순한 경우 확률 누적

시간 복잡도: O(4 * 3^13) = O(600만) ok

"""