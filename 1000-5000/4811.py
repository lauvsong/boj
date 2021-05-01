# 알약
import sys
input = sys.stdin.readline

nums = []
while True:
    N = int(input())
    if N == 0: break
    nums.append(N)

MAX = max(nums) + 1
dp = [[0]*MAX for _ in range(MAX)]
dp[0] = [1]*MAX

for h in range(1,MAX):
    for w in range(h,MAX):
        dp[h][w] = dp[h-1][w] + dp[h][w-1]

for n in nums:
    print(dp[n][n])

"""
문제 상황: 할아버지가 약을 다시 담음

알을 다 쪼개려면? -> 결국 n개 모두 쪼개긴 해야함
즉, w가 n개. h 또한 무조건 n개 여야 함

# 정리
w가 n개고, h가 n개이면서 길이가 2n일 때 경우의 수
w: 한 조각
h: 반 조각

# 배열
dp[w][h] : w가 i개고, h가 j개일 때 경우의 수

# 답
dp[W][H]

# 점화식
dp[w][h] = dp[w-1][h] + dp[w][h-1]

# 주의 사항
한개만 있는 경우는 모두 1
반개가 더 많은 경우는 모두 0 (불가능한 경우임)

"""