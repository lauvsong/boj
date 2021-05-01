import sys
input = sys.stdin.readline

N = int(input())
A = tuple(map(int, input().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])

ln = max(dp)
print(ln)

ans = []
for i in range(N-1,-1,-1):
    if dp[i] == ln:
        ans.append(A[i])
        ln -= 1

print(*reversed(ans))