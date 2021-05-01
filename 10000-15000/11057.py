import sys
input = sys.stdin.readline

N = int(input())
dp = [1]*10

for _ in range(N-1):
    for i in range(1,10):
        dp[i] = (dp[i] + dp[i-1]) % 10007

print(sum(dp) % 10007)

"""
# 문제 요약
- 오름차순 조합 구해라

dp[i] : 가장 오른쪽 값이 i일 때 조합수
"""