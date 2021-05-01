import sys
input = sys.stdin.readline

t = int(input())
l = [int(input()) for _ in range(t)]

MAX = max(l)+1
dp = [0]*MAX
dp[0] = 1

for i in range(2,MAX,2):
    for j in range(2,i+1,2):
        dp[i] += (dp[j-2] * dp[i-j]) % 1000000007

for v in l:
    print(dp[v] % 1000000007)


"""
# 괄호
dp[i] : 길이가 i일 때 올바른 괄호 문자열의 개수

# 점화식
dp[l] = dp[i-2] * dp[l-i] (i가 짝수일 때)

(....)[ ]
"""