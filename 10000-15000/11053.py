import sys
input = sys.stdin.readline

N = int(input())
A = tuple(map(int, input().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))

"""
dp[i] : i번째 가 수열의 끝일 때, 최대 부분 수열의 길이
"""