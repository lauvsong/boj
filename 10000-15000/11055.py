import sys
input = sys.stdin.readline

N = int(input())
A = tuple(map(int, input().split()))
dp = [0]*1001

for i in A:
    dp[i] = max(dp[:i]) + i

print(max(dp))

"""
dp[i] : 수열의 끝이 i일 때 최대 합

dp[i] = max(dp[j]+A[i], dp[i])
"""