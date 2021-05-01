import sys
input = sys.stdin.readline

t = int(input())
dp = [0,1,2,4]

for i in range(4,1000001):
    dp.append(sum(dp[-3:]) % 1000000009)


for _ in range(t):
    n = int(input())
    print(dp[n])
