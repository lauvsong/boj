# 외판원 순회
import sys
input = sys.stdin.readline

def dfs(curr, cache):
    if cache == finish:
        if dist[curr][0]: return dist[curr][0]
        else: return 1e9

    if dp[curr][cache] != 1e9: return dp[curr][cache]

    for i in range(1,n):
        if not cache & (1<<i) and dist[curr][i]:
            dp[curr][cache] = min(dp[curr][cache], dfs(i, cache | (1 << i)) + dist[curr][i])

    return dp[curr][cache]

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e9]*(1<<n) for _ in range(n)]
finish = (1 << n) - 1
print(dfs(0,1))

"""
순열 백트래킹 아이디어랑 조금 비슷
dp[현재 방문도시][비트마스크(지금까지 방문한 도시)] = min( dp[i][i까지 방문한 도시] + 현재에서 i까지의 거리 )
"""