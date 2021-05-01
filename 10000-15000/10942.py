import sys
input = sys.stdin.readline

N = int(input())
nums = tuple(map(int, input().split()))
dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if nums[i] == nums[i+1]: 
        dp[i][i+1] == 1

for l in range(2,N):
    for i in range(N-l):
        if nums[i] == nums[i+l] and dp[i+1][i+l-1] == 1:
            dp[i][i+l] = 1

M = int(input())
for _ in range(M):
    S,E = map(int, input().split())
    print(dp[S-1][E-1])

"""
dp[a][b] : a에서 b까지 들어가는 숫자가 팰린드롬인지 아닌지

팰린드롬일 시 dp[a+1][b-1] 가 1이며, 양옆 인덱스 값이 같아야한다.
"""