import sys
input = sys.stdin.readline

n,k = map(int, input().split())
dp = [0]*(k+1)

for _ in range(n):
    w,v = map(int, input().split())
    for i in range(w,k+1):
        dp[i] = max(dp[i-w]+v, dp[i])

print(max(dp))

"""
평범한 배낭

dp[k] : k만큼의 무게에서 물건 최대 가치

dp[k] = max(dp[k-w] + v)
*주의 역순으로 해야함 (오름차순은 이전 값이 사전에 계산되어있을 수 있음)
"""