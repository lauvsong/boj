import sys
input = sys.stdin.readline

n = int(input())
requests = tuple(map(int, input().split()))
m = int(input())

l,r = 0,max(requests)
ans = 0

while l <= r:
    mid = (l+r) // 2
    res = 0
    for req in requests:
        res += mid if req > mid else req
    
    # 총액보다 크다면
    if res > m:
        r = mid - 1
    else: # 총액보다 작다면
        ans = mid
        l = mid + 1

print(ans)

"""
상한액 이분탐색

# 최소
0

# 최대
max(reques..)
"""