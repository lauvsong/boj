import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1,2]

for i in range(3,n+1):
    dp.append(sum(dp[-2:]))

print(dp[n] % 10007)