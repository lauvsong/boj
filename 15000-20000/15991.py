import sys
input = sys.stdin.readline

t = int(input())
n = [int(input()) for _ in range(t)]

MAX = max(n)
MOD = 1000000009

dp = [0,1,2,2,3,3,6]
for i in range(7,MAX+1):
    dp.append(sum(dp[i-2:i-7:-2]) % MOD)

for v in n:
    print(dp[v])