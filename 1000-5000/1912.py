import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

for i in range(1,n):
    nums[i] = max(nums[i-1] + nums[i], nums[i])

print(max(nums))

"""
dp[i]: i번째를 마지막으로 선택했을 때 가장 큰 합
dp[i] = dp[i-1] + nums[i]
"""