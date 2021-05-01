import sys
input = sys.stdin.readline

N = int(input())
A = tuple(map(int, input().split()))

dp, dp2 = [1]*N, [1]*N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])

for i in range(N-1,-1,-1):
    for j in range(i+1,N):
        if A[i] > A[j]:
            dp2[i] = max(dp2[j]+1, dp2[i])

print(max(dp[i]+dp2[i] for i in range(N))-1)