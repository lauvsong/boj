import sys
input = sys.stdin.readline

ans = 1e9
n = int(input())
costLen = n-2

g = []
costs = [[] for _ in range(costLen)]
nearby = [[0]*costLen for _ in range(costLen)]

dx = [-1,-1,-1,0,0,1,1,1,0,0,-2,2,0]
dy = [-1,0,1,-1,1,-1,0,1,-2,2,0,0,0]

def getCost(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cost = g[x][y]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        cost += g[nx][ny]

    return cost

def isInbound(x, y):
    if not 0 <= x < costLen: return False
    if not 0 <= y < costLen: return False

    return True

def visit(x, y):
    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]

        if isInbound(nx, ny):
            nearby[nx][ny] += 1


def leave(x,y):
    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]

        if isInbound(nx, ny):
            nearby[nx][ny] -= 1


def dfs(depth, x, y, cnt):
    global ans
    if depth == 3:
        ans = min(ans, cnt)
        return

    if ans <= cnt:
        return

    for ny in range(y, costLen):
        if nearby[x][ny]: continue
        visit(x, ny)
        dfs(depth+1, x, ny, cnt + costs[x][ny])
        leave(x,ny)

    for nx in range(x+1, costLen):
        for ny in range(costLen):
            if nearby[nx][ny]: continue
            visit(nx, ny)
            dfs(depth+1, nx, ny, cnt + costs[nx][ny])
            leave(nx,ny)


for _ in range(n):
    g.append(list(map(int, input().split())))

for x in range(1,n-1):
    for y in range(1,n-1):
        costs[x-1].append(getCost(x,y))

dfs(0,0,0,0)

print(ans)

"""
# 문제
꽃 3개를 심는 최소 비용

# 제약 조건
1. 꽃은 5칸 비용 합 만큼 차지
2. 꽃끼리 닿으면 X
가장자리 넘으면 X

# 변수
N: 화단 변 길이 (6≤N≤10)
(0<=가격<=200)


5개 합 가장 작은 구역 3개를 고르면 됨. (조합)

단순 그리디 불가.
브루트포스 알고리즘 선택.


# 알고리즘
**DFS**
- 구역 마다 DFS (N=10일 최대 64개 구역)

DFS()
- 64개 구역 중에 3개를 정함
- 끝에서는, 비용합 갱신함
- end : 3개가 됐을 때
- go : i~64 중 하나 choice

O(64^3) = O(26만)
-> 시간초과 X.


# 구현
구역 : 2차원 배열 (N-2) * (N-2)

1. 구역마다 합 구해놓기
2. DFS로 최소 비용 구하기
    - 레벨 : idx ~ (N-2)*(N-2)
    - 깊이 : 3
    - 조건 : 


"""