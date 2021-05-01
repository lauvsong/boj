# 부분합
# 투 포인터
import sys
input = sys.stdin.readline

n,s = map(int, input().split())
nums = tuple(map(int, input().split()))
one, two = 0, 0
ans = sys.maxsize
res = 0

while True:
    if res >= s:
        ans = min(ans, two-one)
        res -= nums[one]
        one += 1
    elif two == n:
        break
    else:
        res += nums[two]
        two += 1
    
print(ans if ans != sys.maxsize else 0)