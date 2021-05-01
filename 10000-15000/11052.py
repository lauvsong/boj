import sys
input = sys.stdin.readline

N = int(input())
p = [0] + list(map(int, input().split()))

for i in range(1,N+1):
    p[i] = max(p[j] + p[i-j] for j in range(i//2, i+1))

print(p[N])

"""
# 문제 요약
- 주어진 수열의 부분합 중 최댓값을 구해라

dp[i] 
i : 카드 개수

# 점화식
dp[i] = max(dp[i], dp[j] + dp[i-j])
"""