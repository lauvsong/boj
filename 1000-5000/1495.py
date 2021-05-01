import sys
input = sys.stdin.readline

N,S,M = map(int, input().split())
v = [0] + list(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j] == 0: continue
        if j+v[i] <= M:
            dp[i][j+v[i]] = 1
        if 0 <= j-v[i]:
            dp[i][j-v[i]] = 1

ans = -1
for i in range(M+1)[::-1]:
    if dp[-1][i]:
        ans = i
        break

print(ans)

"""
기타리스트

dp[n][i] : n번째 곡에서 볼륨 i로 연주 가능 여부

케이스
1. +v[i]
2. -v[i]

dp[n][i] = dp[]

*끝까지 최대를 알 수 없을 때는, 가능 여부를 체크하게 하는 것도 괜찮은듯
"""