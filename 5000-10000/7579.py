import sys
input = sys.stdin.readline

ans = 1e9

n,m = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split())) 

tc = sum(costs)

dp = [[0]*(tc+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, tc+1):
        if j < costs[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i]] + mems[i])

        if m <= dp[i][j]:
            ans = min(ans, j)

print(ans)

"""
# 문제
m 바이트를 확보하기 위한 최소 비용(c) 출력

# 변수
n : 활성화된 앱 개수
m : 필요한 바이트 수


# 점화식 (실패)
dp[i]: i 바이트까지 확보한 최소 비용

dp[i] = min(dp[i], dp[i-m] + c)


for i 끝,m:
	dp[i] = min(dp[i], dp[i-m] + c)


시간초과.

---


# 점화식 2.
dp[i][j] : i번째 앱까지 비용 j로 얻을 수 있는 '최대' 메모리

dp[i][j] = max(dp[i][j], dp[i-1][j-cost] + mem)

"""