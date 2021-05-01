import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*101
dp[0] = 0; dp[1] = 1; dp[2] = 2; dp[3] = 3;

for i in range(4,N+1):
    for j in range(2,i-2):
        dp[i] = max(dp[i-1]+1, j*dp[i-(j+1)], dp[i])

print(dp[N])

"""
# 크리보드

뭐고 개어렵두 ㅜㅜ ㅅㅂ
왜 실버임 ㅅㅂ 아
계속 마지막 경우를 생각해야 할듯

d[n] : n번 눌러서 출력할 수 있는 A의 최대 개수

# 점화식
d[i] = max(d[i-1]+1, j*d[n-(j+1)])

아 존나 힘들었다...
"""