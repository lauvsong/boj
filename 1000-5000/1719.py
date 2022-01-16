import sys
input = sys.stdin.readline

def init():
    for _ in range(m):
        src, dst, weight = map(int, input().split())
        graph[src][dst] = graph[dst][src] = weight
        ans[src][dst] = dst
        ans[dst][src] = src


def present():
    for nums in ans[1:]:
        print(*nums[1:])

def floydWarshall():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i == j: continue
                result = graph[i][k] + graph[k][j]
                if graph[i][j] <= result: continue

                graph[i][j] = graph[j][i] = result
                ans[i][j], ans[j][i] = ans[i][k], ans[j][k]

def solve():
    init()
    floydWarshall()
    present()
 
n,m = map(int, input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]
ans = [["-"]*(n+1) for _ in range(n+1)]

solve()


"""
택배

# 문제
- 경로표를 구해라.


경로표 : 집하장->집하장 최단경로 중 가장 먼저 거치는 집하장


# 입력
n: 집하장의 개수
m: 집하장 간 경로의 개수


노드1, 노드2, 가중치


---

모든 정점 : 모든 정점 -> 플로이드 워셜.


# 반복문
거쳐가는 정점
- 시작점
- 종료점

첫 집하장 기록.


"""